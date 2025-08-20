import os
import pytest
import pathlib
from config.env_config import setup_env

@pytest.fixture(scope="session", autouse=True)
def load_env_for_integration():
    """
    Integration tests should use the dev environment by default.
    This fixture force-loads .env.dev from the project root and
    fails loudly (instead of skipping) if it cannot be found so we
    can see why.
    """
    # Force dev to avoid surprises from ENV being set elsewhere
    env = "dev"

    # Resolve project root: .../tests/integration_tests -> .../tests -> project root
    project_root = pathlib.Path(__file__).resolve().parents[2]
    env_file = project_root / ".env.dev"

    # Debug prints (visible with `-s`)
    print(f"[integration setup] ENV={env}")
    print(f"[integration setup] project_root={project_root}")
    print(f"[integration setup] env_file={env_file}")

    if not env_file.exists():
        # Show the directory contents to help debug path issues
        try:
            contents = [str(p.name) for p in project_root.iterdir()]
        except Exception as ex:
            contents = [f"<error listing project_root: {ex}>"]
        print(f"[integration setup] project_root contents: {contents}")
        pytest.fail(f"Expected env file not found at: {env_file}")

    # Ensure relative paths inside setup_env() resolve correctly
    os.chdir(project_root)

    # Load variables using your central loader
    setup_env(["pytest", env])
    print(f"[integration setup] loaded {env_file}")