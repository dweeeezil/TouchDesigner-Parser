import os
from pathlib import Path

for root, dirs, files in os.walk(Path.home() / "Desktop" / "TDA_lights" / "TDA_lights.toe.dir"):
    if files:
        print(root, files)