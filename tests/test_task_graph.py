import unittest

from metal.structs import TaskGraph, SingleTaskGraph

class TaskGraphTest(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     pass

    # @classmethod
    # def tearDownClass(cls):
    #     pass

    def test_single_task(self):
        tg = SingleTaskGraph(k=3)
        self.assertTrue(tg == TaskGraph([], [3]))
        # self.assertTrue(tg.depth == 0)

    def test_binary_tree(self):
        cardinalities = [2,2,2]
        edges = [(0,1), (0,2)]
        tg = TaskGraph(edges, cardinalities)
        self.assertTrue(tg.parents[0] == [])
        self.assertTrue(tg.parents[1] == [0])
        self.assertTrue(tg.parents[2] == [0])
        self.assertTrue(tg.children[0] == [1,2])
        self.assertTrue(tg.children[1] == [])
        self.assertTrue(tg.children[2] == [])
        # self.assertTrue(tg.depth == 1)
        
    def test_nonbinary_tree(self):
        cardinalities = [3,2,2,2]
        edges = [(0,1), (0,2), (0,3)]
        tg = TaskGraph(edges, cardinalities)
        self.assertTrue(tg.parents[1] == [0])
        self.assertTrue(tg.children[0] == [1,2,3])
        # self.assertTrue(tg.depth == 1)

    def test_binary_tree_depth3(self):
        cardinalities = [2,2,2,2,2,2,2]
        edges = [(0,1), (0,2), (1,3), (1,4), (2,5), (2,6)]
        tg = TaskGraph(edges, cardinalities)
        self.assertTrue(tg.parents[1] == [0])
        self.assertTrue(tg.children[1] == [3, 4])
        # self.assertTrue(tg.depth == 2)

    def test_unbalanced_tree(self):
        cardinalities = [2,2,2]
        edges = [(0,1), (1,2)]
        tg = TaskGraph(edges, cardinalities)
        self.assertTrue(tg.parents[1] == [0])
        self.assertTrue(tg.children[1] == [2])
        # self.assertTrue(tg.depth == 2)

        
if __name__ == '__main__':
    unittest.main()