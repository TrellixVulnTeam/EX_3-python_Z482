
import unittest
from unittest import TestCase
from src.DiGraph import DiGraph
from src.Node_data import Node_data,geo_location

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = DiGraph()
        self.graph1=DiGraph()


    def test_graph(self):
        for n in range(1000):
            self.graph.add_node(node_id=n,pos=(n + 1, n - 1, 0))
        self.assertEqual(1000, self.graph.v_size())
        self.graph.add_node(0)
        self.assertEqual(1000, self.graph.v_size())
        self.graph.remove_node(0)
        self.assertEqual(999, self.graph.v_size())
        for n in range(0,1000):
            self.graph.remove_node(n)
        self.assertEqual(0, self.graph.v_size())
        self.graph.add_node(0, None)
        self.graph.add_node(1, None)
        self.graph.add_node(2, None)

        self.assertEqual(3, self.graph.v_size())
        self.graph.remove_node(0)
        self.assertEqual(2004, self.graph.get_mc())
        self.graph.add_edge(0, 1, 0)
        self.graph.add_edge(1, 2, 0)
        self.graph.add_edge(2, 0, 0)
        self.graph.remove_edge(0, 1)
        self.assertEqual(1, self.graph.num_of_edges)
        self.graph.remove_node(1)
        self.assertEqual(0, self.graph.num_of_edges)
        for n in range(0,3):
            self.graph.remove_node(n)
        self.assertEqual(0, self.graph.v_size())
        for n in range(1000000):
            self.graph.add_node(n)
            if n % 100 == 0:
                self.graph.add_node(n) ## the key exist
        self.assertEquals(1000000, self.graph.v_size())
        for i in range (10,20):

            self.graph.remove_node(i)
            self.graph.remove_node(i)

        self.assertEquals((1000000-10), self.graph.v_size())



    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
