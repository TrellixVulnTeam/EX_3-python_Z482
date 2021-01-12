import unittest
import json
from src.DiGraph import DiGraph
import networkx as nx
from src.GraphAlgo import GraphAlgo
import random
import time

class MyTestCase(unittest.TestCase):

    def from_json_to_nx(self,file_name):
        graph = nx.DiGraph()
        try:
            with open(file_name, "r") as f:
                jsonfile = json.load(f)
                edges = jsonfile["Edges"]
                nodes = jsonfile["Nodes"]
                for n in nodes:
                    graph.add_node(n["id"])
                for e in edges:
                    graph.add_weighted_edges_from([(e["src"], e["dest"], e["w"])])
            return graph
        except IOError as e:
            print(e)
            return None

    def Test_loading_10(self, filename, graph_name):

        graph_nx= self.from_json_to_nx(filename)

        ga= GraphAlgo()
        ga.load_from_json(filename)

        src = random.randint(0, ga.get_graph().v_size()-1)
        dest = random.randint(0, ga.get_graph().v_size()-1)

        ############################## connected_components############################

        #our time
        start_time=time.time()

        algo_comp = ga.connected_components()

        end_time=time.time()
        algotime=end_time-start_time

        #nx time
        start_time = time.time()

        nx_comp=list(nx.strongly_connected_components(graph_nx))

        end_time = time.time()
        nx_time = end_time - start_time

        print("for graph "+ graph_name +" in components function our time is ","{:.10f}".format(algotime),"and nx time is:","{:.10f}".format(nx_time) )


        self.assertEqual(set(tuple(i) for i in nx_comp),set(tuple(i) for i in algo_comp))

        ###################################shortest_path###################################

        start_time = time.time()

        dist_algo, path_algo= ga.shortest_path(src, dest)

        end_time = time.time()
        algotime1 = end_time - start_time

        start_time=time.time()

        dist_nx= nx.shortest_path_length(graph_nx, src, dest, weight='weight')
        path_nx= nx.dijkstra_path(graph_nx,src,dest,weight="weight")

        end_time=time.time()
        nx_time1 = end_time - start_time

        print("for graph "+ graph_name +" in shortest path function our time is ", "{:.10f}".format(algotime1), "and nx time is:", "{:.10f}".format(nx_time1))

        self.assertEqual(dist_algo,dist_nx)
        self.assertEqual(path_algo,path_nx)

        ####################single node component##############
        # our time
        start_time = time.time()

        ga.connected_component(src)

        end_time = time.time()
        algotime2 = end_time - start_time
        print("for graph " + graph_name + " in single node component our time is ", "{:.10f}".format(algotime2))

    def test_all(self):
        self.Test_loading_10("../data/G_10_80_1.json", "G_10")
        self.Test_loading_10("../data/G_100_800_1.json","G_100")
        self.Test_loading_10("../data/G_1000_8000_1.json","G_1000")
        self.Test_loading_10("../data/G_10000_80000_1.json","G_10000")
        self.Test_loading_10("../data/G_20000_160000_1.json","G_20000")
        self.Test_loading_10("../data/G_30000_240000_1.json","G_30000")

    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
