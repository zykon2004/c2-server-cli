import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[2] / "c2-server" / "server"))
print(sys.path)
