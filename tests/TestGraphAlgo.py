import math
import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = None
        self.ga = GraphAlgo()

    def test_algo(self):
        self.assertEqual(True,self.ga.load_from_json("../data/T0.json"))
        self.assertEqual(True, self.ga.save_to_json("test.json"))
        self.assertEqual(self.ga.get_graph().v_size(),4)
        self.assertEqual(self.ga.get_graph().e_size(), 5)

        self.assertEqual((2.8, [0, 1, 3]), self.ga.shortest_path(0, 3))
        self.assertEqual((math.inf, []), (self.ga.shortest_path(3, 1)))

        self.assertEqual([[0, 1], [2], [3]],self.ga.connected_components())
        self.assertEqual([0, 1], self.ga.connected_component(1))
        self.ga.plot_graph()




    def test_something(self):
        self.assertEqual(True,True)


if __name__ == '__main__':
    unittest.main()
