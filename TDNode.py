

class TDNode:
    def __init__(self, name, op_type, path):
        self.name = name
        self.op_type = op_type
        self.path = path

        self.parameters = {}
        self.inputs = []
        self.outputs = []
        self.script = None
