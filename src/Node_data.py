from DiGraph import DiGraph
class Node_data :
    def __init__(self,key: int,tag:int=None,info:str = "white" , weight: float =0,pos:tuple=None ):
        self.key=key
        self.tag=tag
        self.info=info
        self.weight=weight
        self.pos=pos;

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
    def __repr__(self):
        return f"pos:{self.pos},id:{self.key}"