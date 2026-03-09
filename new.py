

from pathlib import Path
import os
import json

from TDNode import TDNode
from TDProject import TDProject



def parseProjectDirectory(root_dir):
    project = TDProject()
    root_dir = Path(root_dir).expanduser()

    for root, dirs, files in os.walk(root_dir):
        for file in files:

            if not file.endswith(".n"):
                continue

            node_name = file[:-2]
            node = TDNode(node_name, root)
            print(file)


    return



parseProjectDirectory('')