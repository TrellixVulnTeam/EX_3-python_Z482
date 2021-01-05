from src.GraphInterface import GraphInterface

import math
class DiGraph(GraphInterface):

    def __init__(self,mc:int=0,num_of_edges: int=0, my_nodes: dict={}, edges_in: dict={},edges_out: dict={},edges: list=[],nodes: list=[]):
        self.mc=mc
        self.nodes=nodes
        self.num_of_edges=num_of_edges
        self.my_nodes=my_nodes
        self.edges_in=edges_in
        self.edges_out=edges_out
        self.edges=edges

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if pos!= None:
            x,y,z=pos
            pos=geo_location(x,y,z)
        if node_id not in self.my_nodes:
            n=Node_data(key=node_id, pos=pos)
            self.my_nodes[node_id]= n
            self.edges_out[node_id]={}
            self.edges_in[node_id]={}
            self.nodes.append({"pos":""+str(x)+","+str(y)+","+str(z)+"","id":self.my_nodes[node_id].key})
            self.mc+=1
            return True
        else:
            return False

    def v_size(self) -> int:
        return len(self.my_nodes)

    def e_size(self) -> int:
        return self.num_of_edges

    def get_all_v(self) -> dict:
        return self.my_nodes

    def get_mc(self) -> int:
        return self.mc

    def remove_node(self, node_id: int) -> bool:
        if node_id  in self.my_nodes :
            for key in list(self.edges_out.get(node_id)):
                del self.edges_in.get(key)[node_id]
            for key in list(self.edges_in.get(node_id)):
                del self.edges_out.get(key)[node_id]
            self.num_of_edges-= len(self.edges_out[node_id])
            del self.edges_out[node_id]
            self.num_of_edges -= len(self.edges_in[node_id])
            del self.edges_in[node_id]

            self.nodes.remove({"pos":self.my_nodes[node_id].pos,"id":self.my_nodes[node_id].key})
            del self.my_nodes[node_id]
            self.mc += 1

            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1!=node_id2 and node_id2 in self.my_nodes and node_id1 in self.my_nodes and node_id2 in self.edges_out.get(node_id1):
            self.mc=+1
            self.num_of_edges-=1
            self.edges.remove({"src": node_id1, "w": self.edges_out.get(node_id1)[node_id2], "dest": node_id2})
            del self.edges_in.get(node_id2)[node_id1]
            del self.edges_out.get(node_id1)[node_id2]

            return True
        else: return  False



    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1  in self.my_nodes and id2  in self.my_nodes and id1!=id2 and weight>=0 :
            if id2 not in self.edges_out.get(id1):
                self.num_of_edges+=1
                self.edges_out.get(id1)[id2] = weight
                self.edges_in.get(id2)[id1] = weight
                self.edges.append({"src":id1,"w":weight,"dest":id2})
                self.mc+=1
                return True
        return False

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 in self.my_nodes:
            return self.edges_in.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self.my_nodes:
            return self.edges_out.get(id1)

    def __str__(self) -> str:
        return f"Graph :|V| ={self.v_size()}, |E|={self.e_size()}"


class geo_location:

    def __init__(self, x: int = 0, y: int = 0, z : int =0):
        self.y = y
        self.x = x
        self.z =z


class Node_data :
    def __init__(self,key: int,tag:int=None,info:str = "white" , weight: float =math.inf,pos: geo_location = None ):
        self.key=key
        self.tag=tag
        self.info=info
        self.weight=weight
        self.pos=pos


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
    #     return f"{self.key}: {self.key} |edges out| {self.graph.all_out_edges_of_node(self.graph,self.key).values()} |edges in| {self.graph.all_in_edges_of_node(self.graph,self.key).values()} "
    #
    def __lt__(self, other):
        return self.weight< other.weight

    def __gt__(self, other):
        return self.weight > other.weight
    def __cmp__(self, other):
        return int.cmp(self.weight,other.weight)
