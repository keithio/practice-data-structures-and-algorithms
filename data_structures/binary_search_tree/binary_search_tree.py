from sys import maxint as MAXINT


MININT = -(MAXINT + 1)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.visited = False

    def __str__(self):
        return str(self.value)

    def __get__(self):
        return self.value


class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, root=None):
        """
        Inserts a new node in the binary search tree.
        """

        root = root if root else self.root

        if not self.root:
            # Need to insert at tree root
            self.root = Node(node)
        elif node.value < root.value:
            # Need to insert on the left side
            if root.left:
                self.insert(node, root.left)
            else:
                root.left = node
        else:
            # Need to insert on the right side
            if root.right:
                self.insert(node, root.right)

    def is_valid(self, from_node=None):
        """
        Determines if the tree is a valid BST.
        """
        from_node = from_node if from_node else self.root
        return self._is_valid(from_node)

    def _is_valid(self, node, minint=MININT, maxint=MAXINT):
        """
        Determines if the tree is valid and recursively searches down.
        """
        # # Check if the left is valid
        # left_invalid = (node.left and
        #                 ((node.left.value < minint) or
        #                   self._is_valid(node.left, minint, node.value)))
        # if left_invalid: return False

        # # Check if the right is invalid
        # right_invalid = (node.right and
        #                  ((node.right.value > maxint) or
        #                    self._is_valid(node.right, node.value, maxint)))
        # if right_invalid: return False

        # return True
        try:
            if node.left.value < minint:
                print 1
                raise Exception
            if not self._is_valid(node.left, minint, node.value):
                print 2
                raise Exception
        except:
            pass

        try:
            if node.right.value > maxint:
                print 3
                raise Exception
            if not self._is_valid(node.right, node.value, maxint):
                print 4
                raise Exception
        except:
            pass

        return True



# from compiler.ast import flatten


# class BinarySearchTreeNode:
#     def __init__(self, value, left=None, right=None):
#         self.left = left
#         self.right = right
#         self.value = value


# class BinarySearchTree:
#     def __init__(self, parent=None):
#         self.parent = parent

#     def insert(self, node, parent=None):
#         """
#         Inserts a new value in the binary search tree.
#         """
#         parent = parent if parent else self.parent

#         if not parent:
#             # Need to insert root node
#             self.parent = node
#         elif node < parent.value:
#             # Need to insert on the left side
#             if not parent.left:
#                 parent.left = node
#             else:
#                 self.insert(node, parent.left)
#         else:
#             # Need to insert on the right side
#             if not parent.right:
#                 parent.right = node
#             else:
#                 self.insert(node, parent.right)

#     def nodes_in_order(self):
#         result = self._nodes_in_order(self.parent)
#         return [x for x in flatten(result) if x]

#     def _nodes_in_order(self, node):
#         result = []
#         if node is not None:
#             left = self._nodes_in_order(node.left)
#             right = self._nodes_in_order(node.right)
#             if left:
#                 result.append(left)
#             result.append([node.value])
#             if right:
#                 result.append(right)
#         return result

#     def nodes_pre_order(self):
#         result = self._nodes_pre_order(self.parent)
#         return [x for x in flatten(result) if x]

#     def _nodes_pre_order(self, node):
#         result = []
#         if not node:
#             return None
#         result.append([node.value])
#         result.append(self._nodes_in_order(node.left))
#         result.append(self._nodes_in_order(node.right))
#         return result

#     def print_in_order(self):
#         print self.nodes_in_order()
