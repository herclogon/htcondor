import sys
import pytest
from .scripts import SCRIPTS

# This module is loaded as a "plugin" by pytest by a setting in conftest.py
# Any fixtures defined here will be globally available in tests,
# as if they were defined in conftest.py itself.


@pytest.fixture(scope="session")
def path_to_sleep():
    return SCRIPTS["sleep"]


@pytest.fixture(scope="session")
def path_to_python():
    return sys.executable
