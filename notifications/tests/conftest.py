import sys

from pathlib import Path

CWD = Path(__file__).resolve().parent
CODE_DIR = CWD / '../src'

sys.path.append(str(CODE_DIR))
