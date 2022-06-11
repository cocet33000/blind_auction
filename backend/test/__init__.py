from pathlib import Path
import sys

# add base project path to PYTHONPATH
BASE_DIR = Path(__file__).resolve().parent.parent / "main"
sys.path.append(str(BASE_DIR))
