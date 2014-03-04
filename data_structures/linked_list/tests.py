#!/usr/bin/env python
import unittest
from linked_list import LinkedList


class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()
        for i in range(1, 6):
            self.ll.append(i)

    def test_creation(self):
        self.assertEqual(5, len(self.ll))

    def test_pop_value(self):
        self.assertEqual(1, self.ll.pop())

    def test_pop_length(self):
        self.ll.pop()
        self.assertEqual(4, len(self.ll))

    def test_push_value(self):
        self.ll.push(0)
        self.assertEqual(0, self.ll.get_head().value)

    def test_push_length(self):
        self.ll.push(0)
        self.assertEqual(6, len(self.ll))

    def test_remove_length(self):
        node = self.ll.get_head().next.next
        self.ll.remove(node)
        self.assertEqual(4, len(self.ll))

    def test_distinct(self):
        self.assertEqual([1, 2, 3, 4, 5], self.ll.distinct())

    def test_distinct_with_duplicate(self):
        self.ll.append(1)
        self.assertEqual([1, 2, 3, 4, 5], self.ll.distinct())

    def test_cycle_false(self):
        self.assertEqual(False, self.ll.has_cycle())

    def test_cycle_true(self):
        last_node = self.ll.get_tail()
        last_node.next = self.ll.get_head()
        self.assertEqual(True, self.ll.has_cycle())



if __name__ == '__main__':
    unittest.main()