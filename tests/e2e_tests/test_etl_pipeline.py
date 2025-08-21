import subprocess
import sys
import os
from pathlib import Path
import pandas as pd

# e2e tests to check if etl pipeline works correctly

def test_etl_pipeline_success(tmp_path):
    # set up test environment
    env = os.environ.copy()
    env["ENV"] = "dev"
    # redirect IO to temp folders so we don't touch real data/
    env["RAW_DIR"] = str(tmp_path / "raw")
    env["OUTPUT_DIR"] = str(tmp_path / "processed")
    # optional: skip load step during tests if your script supports it
    env["SKIP_LOAD"] = "1"

    # get project root
    project_root = Path(__file__).parent.parent.parent

    # run etl pipeline script
    result = subprocess.run(
        [sys.executable, "scripts/run_etl.py", "dev"],
        cwd=str(project_root),
        env=env,
        capture_output=True,
        text=True,
    )

    # verify script ran successfully
    assert result.returncode == 0, f"ETL pipeline failed:\nSTDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"

    # verify output file exists (in temp processed dir)
    output_file = tmp_path / "processed" / "clean_oscars.csv"
    assert output_file.exists(), f"Expected output file not created: {output_file}"

    # verify output file is not empty & has expected column
    result_df = pd.read_csv(output_file)
    assert not result_df.empty, "Output file is empty"
    assert "ceremony" in result_df.columns, "Missing expected column in output"


# test that checks if the piepeline fails with an invalid environment
def test_etl_pipeline_invalid_environment():
    env = os.environ.copy()

    project_root = Path(__file__).parent.parent.parent

    # run etl pipeline script with invalid environment
    result = subprocess.run(
        [sys.executable, "scripts/run_etl.py", "invalid_env"],
        cwd=str(project_root),
        env=env,
        capture_output=True,
        text=True,
    )

    # verify pipeline failed
    assert result.returncode == 1, (
        "ETL pipeline to fail with invalid environment, "
        f"got return code {result.returncode}"
    )
    assert (
        "Please provide an environment" in (result.stderr or "")
        or "Please provide an enviroment" in (result.stdout or "")
    )