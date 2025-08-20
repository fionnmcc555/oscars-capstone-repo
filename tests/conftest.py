import os
import pytest
from config.env_config import setup_env

@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """
    Only load .env.test when ENV=='test' and the file exists.
    Do NOT skip the whole session from here.
    """
    env = os.environ.get("ENV")
    if env == "test" and os.path.exists(".env.test"):
        setup_env(["pytest", "test"])
    # otherwise do nothing
    

