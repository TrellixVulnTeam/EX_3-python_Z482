from src.GraphInterface import GraphInterface

import math
from src.Node_data  import Node_data,geo_location
class DiGraph(GraphInterface):

    def __init__(self):
        self.mc=0
        self.nodes=[]
        self.num_of_edges=0
        self.my_nodes= {}
        self.edges_in= {}
        self.edges_out= {}
        self.edges=[]

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if pos != None:
            x,y,z=pos
            gl=geo_location(x,y,z)
        if node_id not in self.my_nodes.keys():
            n=Node_data(key=node_id)
            self.my_nodes[node_id]= n
            self.edges_out[node_id]={}
            self.edges_in[node_id]={}
            if pos != None:
                n.pos=gl
                self.nodes.append({"pos":""+str(x)+","+str(y)+","+str(z)+"","id":self.my_nodes[node_id].key})
            else:
                self.nodes.append({"id": self.my_nodes[node_id].key})
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

            if self.my_nodes[node_id].pos is not None :
                self.nodes.remove({"pos":""+str(self.my_nodes[node_id].pos.x)+","+str(self.my_nodes[node_id].pos.y)+","+str(self.my_nodes[node_id].pos.z)+"" ,"id":self.my_nodes[node_id].key})
            else:
                self.nodes.append({"id": self.my_nodes[node_id].key})
            del self.my_nodes[node_id]
            self.mc+=1

            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1!=node_id2 and node_id2 in self.my_nodes and node_id1 in self.my_nodes and node_id2 in self.edges_out.get(node_id1):
            self.mc+=1
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

    def __repr__(self):
        lines = 'Nodes: {'
        for key in self.my_nodes:
            lines += ' ' + str(key) + ' ,'
        lines += ' }\n'

        lines += 'EdgesOut: {'
        for key, value in self.edges_out.items():
            print('key ' + str(key))
            print('value' + str(value))

            lines += ' ' + str(key) + ' : '
            for neighbour in self.edges_out[key]:
                lines += ' ' + str(neighbour) + ' ,'
        lines += ' } '

        return lines


