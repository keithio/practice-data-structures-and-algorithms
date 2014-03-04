#!/usr/bin/env python
import unittest
from binary_search_tree import BST, Node


class BSTTest(unittest.TestCase):

    def setUp(self):
        self.bst = BST()
        # node0 = BinarySearchTreeNode(1)
        # node1 = BinarySearchTreeNode(2)
        # node2 = BinarySearchTreeNode(3)
        # node3 = BinarySearchTreeNode(4)
        # node4 = BinarySearchTreeNode(5)
        # self.bst.insert(node0)
        # self.bst.insert(node4)
        # self.bst.insert(node2)
        # self.bst.insert(node1)
        # self.bst.insert(node3)

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