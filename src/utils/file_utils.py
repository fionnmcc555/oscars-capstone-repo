import pandas as pd
import os

def find_project_root(marker_file="README.md"):
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while current_dir != os.path.dirname(current_dir):
        if marker_file in os.listdir(current_dir):
            return current_dir
        current_dir = os.path.dirname(current_dir)
    raise FileNotFoundError(
        f"Marker file '{marker_file}' not found in any parent directories."
    )


ROOT_DIR = find_project_root()
INDEXES_PATH = os.path.join(ROOT_DIR, "etl", "sql", "indexes")
QUERY_PATH = os.path.join(ROOT_DIR, "etl", "sql")


def save_dataframe_to_csv(df: pd.DataFrame, relative_output_dir: str, filename: str) -> None:
    output_dir = os.path.join(ROOT_DIR, relative_output_dir)
    os.makedirs(output_dir, exist_ok=True)
    df.to_csv(os.path.join(output_dir, filename), index=False)
    print(f"Data saved to {os.path.join(output_dir, filename)}")