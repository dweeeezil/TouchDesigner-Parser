import os
import json
from pathlib import Path


class TDNode:
    def __init__(self, name, folder):
        self.name = name
        self.folder = folder
        self.parameters = {}
        self.script = None


class TDProject:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node


def parse_parameters(path): # Parses parameters for a given path to a node

    params = {}

    if not os.path.exists(path):
        return params

    with open(path, "r", encoding="utf8", errors="ignore") as f:
        for line in f:
            if "\t" in line:
                k, v = line.split("\t", 1)
                params[k.strip()] = v.strip()

    return params


def find_script(folder, node_name): #Finds the script files for a given node

    script_extensions = [".text", ".script", ".py"]

    for ext in script_extensions:
        p = os.path.join(folder, node_name + ext)

        if os.path.exists(p):
            with open(p, "r", encoding="utf8", errors="ignore") as f:
                return f.read()

    return None


def parse_toe_directory(root_dir): # Opens project directory, creates node objects for project

    project = TDProject()

    root_dir = Path(root_dir).expanduser()

    for root, dirs, files in os.walk(root_dir):
        for file in files:

            if not file.endswith(".n"):
                continue

            node_name = file[:-2]
            node = TDNode(node_name, root)
            parm_file = os.path.join(root, node_name + ".parm")
            node.parameters = parse_parameters(parm_file)

            node.script = find_script(root, node_name)

            full_path = os.path.join(root, node_name)

            project.nodes[full_path] = node

    return project


def project_to_json(project):

    output = {}

    for path, node in project.nodes.items():

        output[path] = {
            "name": node.name,
            "parameters": node.parameters,
            "script": node.script
        }

    return output


def main():

    project_path = Path.home() / "Desktop/TDA_lights/TDA_lights.toe.dir"

    project = parse_toe_directory(project_path)

    print("Nodes parsed:", len(project.nodes))

    with open("td_project.json", "w") as f:
        json.dump(project_to_json(project), f, indent=2)

    print("JSON exported")


if __name__ == "__main__":
    main()