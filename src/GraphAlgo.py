from DiGraph import DiGraph
from GraphInterface import GraphInterface
from src.GraphAlgoInterface import GraphAlgoInterface
import json
from queue import PriorityQueue

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
                x,y,z= n["pos"].split(",")
                pos=(int(x),int(y),int(z))
                graph.add_node(node_id=n["id"],pos=pos)
            for e in edges:
                graph.add_edge(id1=e["src"],id2=e["dest"],weight=e["w"])
        self.graph=graph

    def shortest_path(self, id1: int, id2: int) -> (float, list):
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

    def dijakstra(self, src:int):
        self.graph.my_nodes[src].tag=0
        q = PriorityQueue()
        for n in self.graph.my_nodes.values():
            q.put(n)
        while not q.empty():
            current_node= q.get()
            print(current_node.key)
            print(self.graph.edges_out[current_node.key].items())
            for nei, w in self.graph.edges_out[current_node.key].items():
                if self.graph.my_nodes[nei].weight> current_node.weight + w:
                    self.graph.my_nodes[nei].weight=current_node.weight + w
                    self.graph.my_nodes[nei].tag= current_node.key           #keep the prev node



if __name__ == '__main__':
    g = DiGraph()  # creates an empty directed graph
    for n in range(4):
        g.add_node(node_id=n,pos=(n+1,n-1,0))

    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(2, 3, 1.1)
    g.add_edge(1, 3, 1.9)
    # print(g.all_out_edges_of_node(1))
    # print(g.edges)
    g.remove_edge(1, 3)
    g.add_edge(1, 3, 10)

    ga=GraphAlgo(g)
    print(ga.shortest_path(0,3))