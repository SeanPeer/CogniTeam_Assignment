import sys
import os
import pytest

# Add the root directory of the project to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    pytest.main()