import os
import sys
import pytest

base_dir = os.path.dirname(__file__) or '.'
sys.path.append("..")

if __name__ == "__main__":
    pytest.main()