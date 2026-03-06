


class TDNode:
    def __init__(self, name, folder):
        self.name = name
        self.folder = folder


        self.type = None
        self.tilePos = [0, 0, 0, 0]
        self.flags = None
        self.color = (0, 0, 0)
        self.parameters = {}
        self.script = None