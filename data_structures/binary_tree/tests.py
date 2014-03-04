#!/usr/bin/env python
import unittest
from binary_tree import BinaryTree, Node


class BSTTest(unittest.TestCase):

    def setUp(self):
        self.bst = BinaryTree(bst=True)

        self.bst.insert(Node(3))
        self.bst.insert(Node(7))
        self.bst.insert(Node(1))
        self.bst.insert(Node(5))
        # self.bst.print_in_order()

    def test_is_valid(self):
        self.assertEqual(True, self.bst.is_valid())

    # def test_nodes_in_order(self):
    #     self.assertEqual([1, 3, 5, 7], self.bst.nodes_in_order())

    # def test_nodes_pre_order(self):
    #     self.assertEqual([1, 4, 2, 3], self.bst.nodes_in_order())


if __name__ == '__main__':
    unittest.main()