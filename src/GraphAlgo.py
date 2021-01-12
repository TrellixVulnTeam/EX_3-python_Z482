import math
from typing import List
import  random
import numpy as np
import matplotlib.pyplot as plt
from src.DiGraph import DiGraph
from src.GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
import json
from queue import PriorityQueue
from src.Node_data import Node_data,geo_location
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
        try:
            with open(file_name, "r") as f:
                jsonfile = json.load(f)
                edges = jsonfile["Edges"]
                nodes = jsonfile["Nodes"]
                for n in nodes:
                    if "pos" in n.keys():
                        x, y, z = n["pos"].split(",")
                        pos = (float(x), float(y), float(z))
                        graph.add_node(node_id=n["id"], pos=pos)
                    else:
                        graph.add_node(node_id=n["id"])
                for e in edges:
                    graph.add_edge(id1=e["src"], id2=e["dest"], weight=e["w"])
            self.graph = graph
            return True
        except IOError as e:
            print(e)
            return False



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
        all_components = []
        for n in self.get_graph().get_all_v().values():
            if n.info!="grey":
                all_components.append(self.connected_component(n.key))

        return all_components




    def connected_component(self, id1: int) -> list:
        if id1 not in self.get_graph().my_nodes:
            return []
        list1=self.bfs(id1)
        list2= self.bfsReverse(id1)
        list3 = []
        temp = list2

        for node in list1:
            if node in temp:
                list3.append(node)
                self.get_graph().my_nodes[node].info="grey"

        return list3


    def bfs(self,src:int):
        self.set_info()
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

    def bfsReverse(self,src:int) -> set:
        self.set_info()
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
        xmin, ymin,xmax,ymax= self.plot_limit()
        for v in self.get_graph().get_all_v().values():
            if v.pos is None:
                x = random.uniform(xmin,xmax)
                y= random.uniform(ymin,ymax)
                v.pos= geo_location(x,y,0)

        x_pos=[]
        y_pos=[]

        for n in self.get_graph().get_all_v().values():
            x_pos.append(n.pos.x)
            y_pos.append(n.pos.y)


        x_arr= np.array(x_pos)
        y_arr= np.array(y_pos)

        fig, ax = plt.subplots()

        for src in self.get_graph().edges_out.keys():
            for dest in self.get_graph().edges_out[src].keys():


                x1 = self.get_graph().my_nodes[src].pos.x
                y1 = self.get_graph().my_nodes[src].pos.y
                x2 = self.get_graph().my_nodes[dest].pos.x
                y2 = self.get_graph().my_nodes[dest].pos.y
                ax.annotate("",
                            xy=(x2, y2), xycoords='data',
                            xytext=(x1,y1), textcoords='data',
                            arrowprops=dict(arrowstyle="->",
                                            connectionstyle="arc3"),
                            )
        ax.plot(x_arr,y_arr,'o')

        plt.show()

    def plot_limit(self):

        x_pos=[]
        y_pos = []
        for node in self.get_graph().get_all_v().values():
            if node.pos != None:
                x_pos.append(node.pos.x)
                y_pos.append(node.pos.y)
        if len(x_pos) !=0:
            return (min(x_pos),min(y_pos), max(x_pos),max(y_pos))
        else:
            return (0,0,self.get_graph().v_size(),self.get_graph().v_size())

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

