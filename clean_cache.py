import os
import shutil

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

if __name__ == "__main__":
    clean_pycache()