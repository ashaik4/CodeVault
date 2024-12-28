# conftest.py
# 
"""
1.  Deletes all __pycache__ directories and .pyc/.pyo files.
2.	pytest_cleanup Fixture:
    •	A session-scoped fixture that runs once per test session.
	•	Uses yield to separate cleanup before and after tests.
3.	autouse=True:
	•	Automatically applies the fixture to all test runs without explicitly declaring it.
"""
import os
import shutil
import pytest

def clean_pycache(root="."):
    """Recursively delete __pycache__ directories and .pyc/.pyo files."""
    for dirpath, dirnames, filenames in os.walk(root):
        # Remove __pycache__ directories
        if "__pycache__" in dirnames:
            shutil.rmtree(os.path.join(dirpath, "__pycache__"))
        
        # Remove .pyc and .pyo files
        for file in filenames:
            if file.endswith((".pyc", ".pyo")):
                os.remove(os.path.join(dirpath, file))

@pytest.fixture(scope="session", autouse=True)
def cleanup_pycache():
    """Run cleanup before or after the pytest session."""
    # Perform cleanup before running tests
    clean_pycache()
    yield
    # Perform cleanup after running tests (optional)
    clean_pycache()