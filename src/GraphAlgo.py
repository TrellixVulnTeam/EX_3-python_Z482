import math
from typing import List
import  random
import numpy as np
import matplotlib.pyplot as plt
from DiGraph import DiGraph
from GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
import json
from queue import PriorityQueue
from Node_data import Node_data,geo_location
from heapq import heappush, heappop ,heapify

class GraphAlgo(GraphAlgoInterface):
    def __init__(self, graph: DiGraph = DiGraph()):
        self.graph=graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def save_to_json(self, file_name: str) -> bool:

        try:
            with open(file_name,"w")as f:
                edges=self.graph.edges
                nodes=self.graph.nodes
                jsongraph={"Edges": edges,"Nodes":nodes}
                json.dump(jsongraph, indent=4, fp=f)
                return True
        except IOError as e:
            print(e)
            return False

    def load_from_json(self, file_name: str) -> bool:
        graph = DiGraph()
        with open(file_name, "r") as f:
            jsonfile = json.load(f)
            edges=jsonfile["Edges"]
            nodes = jsonfile["Nodes"]
            for n in nodes:
                if "pos" in n.keys():
                    x,y,z= n["pos"].split(",")
                    pos=(float(x),float(y),float(z))
                    graph.add_node(node_id=n["id"],pos=pos)
                else:
                    graph.add_node(node_id=n["id"])
            for e in edges:
                graph.add_edge(id1=e["src"],id2=e["dest"],weight=e["w"])
        self.graph=graph

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        self.set_info()
        self.set_weight()
        self.set_tag()
        if id1  in self.graph.my_nodes and id2  in self.graph.my_nodes:

            if id1==id2 : return(0,[id1])
            self.dijakstra(id1)
            path =[]
            current_node=id2
            dist = self.graph.my_nodes[current_node].weight

            if self.graph.my_nodes[id2].tag!= None:
                while self.graph.my_nodes[current_node].tag!=None:
                    path.append(current_node)
                    current_node=self.graph.my_nodes[current_node].tag
                path.append(id1)
            path.reverse()
            return (dist,path)

        return (float('inf'),[])

    def dijakstra(self, src: int):
        q = PriorityQueue()
        self.graph.my_nodes[src].tag=None
        q.put(self.graph.my_nodes[src])
        self.graph.my_nodes[src].weight = 0
        while not q.empty():
            current_node = q.get()
            for nei, w in self.graph.edges_out[current_node.key].items():
                if self.graph.my_nodes[nei].weight > current_node.weight + w:
                    self.graph.my_nodes[nei].weight = current_node.weight + w

                    self.graph.my_nodes[nei].tag = current_node.key
                    q.put(self.graph.my_nodes[nei])

    def connected_components(self) -> List[list]:
        components_per_node=[]
        for node in self.get_graph().get_all_v().keys():
            components_per_node.append(self.connected_component(node))
        all_components=[]
        for component in components_per_node:
            if component not  in all_components:
                all_components.append(component)
        return all_components
    def connected_component(self, id1: int) -> list:
        if id1 not in self.get_graph().my_nodes:
            return []
        list1=self.bfs(id1)
        list2= self.bfsReverse(id1)
        return list(set(list1)& set(list2))

    def bfs(self,src:int):
        self.set_info()
        self.set_weight()
        self.set_tag()
        myset = {src}
        q=[src]
        self.get_graph().my_nodes[src].info="black"  #the node is visisted
        while len(q) :
            node=q.pop()
            for nei in self.get_graph().all_out_edges_of_node(node).keys():
                if self.get_graph().my_nodes[nei].info=="white":
                    self.get_graph().my_nodes[nei].info = "black"
                    q.append(nei)
                    myset.add(nei)

        return myset

    def bfsReverse(self,src:int):
        self.set_info()
        self.set_weight()
        self.set_tag()
        myset = {src}
        q=[src]
        self.get_graph().my_nodes[src].info="black"  #the node is visisted
        while len(q) :
            node=q.pop()

            for nei in self.get_graph().all_in_edges_of_node(node).keys():

                if self.get_graph().my_nodes[nei].info=="white":
                    self.get_graph().my_nodes[nei].info = "black"
                    q.append(nei)
                    myset.add(nei)

        return myset

    def set_info(self):
            for node in self.get_graph().get_all_v().values():
                node.info="white"

    def set_tag(self):
            for node in self.get_graph().get_all_v().values():
                node.tag=None
    def set_weight(self):
            for node in self.get_graph().get_all_v().values():
                node.weight= math.inf

    def plot_graph(self) -> None:
        for v in self.get_graph().get_all_v().values():
            if v.pos is None:
                x = random.uniform(0.5, self.graph.v_size())
                y= random.uniform(0.5, self.graph.v_size())
                v.pos= geo_location(x,y,0)

        x_pos=[]
        y_pos=[]

        for n in self.get_graph().get_all_v().values():
            x_pos.append(n.pos.x)
        for n in self.get_graph().get_all_v().values():
            y_pos.append(n.pos.y)
        x_arr= np.array(x_pos)
        y_arr= np.array(y_pos)
        d=(max(x_pos))*(max(y_pos))
        ax = plt.axes()

        for src in self.get_graph().edges_out.keys():
            for dest in self.get_graph().edges_out[src].keys():

                r = 0.0001
                x1 = self.get_graph().my_nodes[src].pos.x
                y1 = self.get_graph().my_nodes[src].pos.y
                x2 = self.get_graph().my_nodes[dest].pos.x
                y2 = self.get_graph().my_nodes[dest].pos.y
                dir_x = (x1 - x2) / math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                dir_y = (y1 - y2) / math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
                x1 = dir_x * (-r) + x1
                y1 = dir_y * (-r) + y1
                x2 = dir_x * r + x2
                y2 = dir_y * r + y2
                ax.arrow(x1, y1, (x2 - x1), (y2 - y1) , head_width=d*0.001, head_length=d*0.01, fc='k', ec='k')


        plt.scatter(x_arr,y_arr,s=d*10)
        plt.show()





if __name__ == '__main__':
    g = DiGraph()  # creates an empty directed graph
    for n in range(4):
        g.add_node(node_id=n)

    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 0)
    g.add_edge(2, 1, 1)
    # g.add_edge(1, 0, 1.1)
    # g.add_edge(1, 2, 1.3)
    # g.add_edge(2, 3, 1.1)
    # g.add_edge(1, 3, 1.9)
    # # print(g.all_out_edges_of_node(1))
    # print(g.edges)
    g.remove_edge(1, 3)
    g.add_edge(1, 3, 10)

    ga=GraphAlgo(g)

    ga.plot_graph()

