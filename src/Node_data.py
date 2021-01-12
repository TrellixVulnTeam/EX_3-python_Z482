import math

class geo_location:

    def __init__(self, x: float = 0, y: float = 0, z : float =0):
        self.y = y
        self.x = x
        self.z =z


class Node_data :
    def __init__(self, key: int ):
        self.key=key
        self.tag=None
        self.info="white"
        self.weight = math.inf
        self.pos=None


    def get_key(self):
        return self.key

    def get_pos(self):
        return self.pos

    def get_tag(self):
        return self.tag

    def get_info(self):
        return self.info

    def get_weight(self):
        return self.weight

    def set_tag(self,tag):
        self.tag=tag

    def set_pos(self,pos):
        self.pos=pos

    def set_info(self, info):
        self.info = info

    def set_weight(self,weight):
        self.weight=weight

    def __str__(self) -> str:
        return str(self.key)
    # def __repr__(self):
    #     return DiGraph.__repr__()

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight
    def __cmp__(self, other):
        return int.cmp(self.weight,other.weight)