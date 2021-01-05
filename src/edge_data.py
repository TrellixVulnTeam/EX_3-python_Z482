from DiGraph import DiGraph
class edge_data:
    def __init__(self, src: int,dest: int, tag: int = 0, info: str = None, weight: float = 0):
        self.src=src
        self.dest=dest
        self.tag = tag
        self.info = info
        self.weight = weight

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_tag(self):
        return self.tag

    def get_info(self):
        return self.info

    def get_weight(self):
        return self.weight

    def set_tag(self, tag):
        self.tag = tag

    def set_info(self, info):
        self.info = info

    def set_weight(self, weight):
        self.weight = weight


