


class TDProject:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.path] = node