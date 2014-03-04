# from stack import Stack
# from .. import stack
from data_structures.stack import Stack


class Node:
    """
    Defines a node for the binary tree.
    """
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return '{}'.format(self.value)

    def get_children(self):
        """
        Returns the children nodes as a list.
        """
        return [self.left, self.right]

    def get_root(self):
        node = self
        if node.is_root():
            return node
        while node.parent:
            node = node.parent
        return node

    def get_siblings(self):
        """
        Returns nodes under the same parent.
        """
        return self.parent.get_children()

    def is_leaf(self):
        """
        Returns true if the node is a leaf node, i.e. has no children.
        """
        return not self.left and not self.right

    def is_root(self):
        """
        Returns true if the node is a root node.
        """
        return self.parent is None


class BinaryTree:
    """
    Defines a binary tree, or a tree in which each node can have at most two
    child nodes.
    """
    def __init__(self, bst=True):
        self.root = None
        self.is_bst = bst
        self.nodes = []

    def __repr__(self):
        return self.get_nodes()

    def insert(self, value, root=None):
        """
        Insert new value. If tree is not a BST, must insert nodes manually.
        """
        if not self.is_bst:
            raise Exception('BinaryTree.insert(<<value>>) may only be used '
                            'when BinaryTree.is_bst=True.')

        root = root if root else self.root

        if isinstance(value, Node):
            node = value
        else:
            node = Node(value)

        if not self.root:
            # Need to set the root node for the tree
            self.root = node
        elif node.value < root.value:
            # Need to insert the new node on the left
            if root.left:
                # Need to add under left node
                self.insert(node, root.left)
            else:
                # Set the left node
                root.left = node
        else:
            # Need to insert the new node on the right
            if root.right:
                # Need to add under right node
                self.insert(node, root.right)
            else:
                # Set the right node
                root.right = node


    def get_balance(self):
        """
        Returns the balance of the tree, or the difference between the max
        depth and the min depth.
        """
        return self.get_max_depth() - self.get_min_depth()

    def get_max_depth(self, node=None, initial=1):
        """
        Setup calculation of the max depth of the tree.
        """
        node = node if node else self.root
        return self._get_max_depth(node)

    def _get_max_depth(self, node):
        """
        Recursively calculates the max depth of the tree.
        """
        if not node:
            return 0
        return 1 + max(self._get_max_depth(node.left),
                       self._get_max_depth(node.right))

    def get_min_depth(self, node=None):
        """
        Recursively calculates the min depth of the tree.
        """
        node = node if node else self.root
        return self._get_min_depth(node)

    def _get_min_depth(self, node):
        """
        Recursively calculates the min depth of the tree.
        """
        if not node:
            return 0
        return 1 + min(self._get_min_depth(node.left),
                       self._get_min_depth(node.right))

    def get_nodes(self, node=None):
        """
        Returns the list of nodes in the tree.
        """
        return self.get_nodes_bfs_preorder(node)

    def get_nodes_bfs_inorder(self, node=None):
        """
        Setup retrieval of nodes using breadth-first search.
        """
        node = node if node else self.root
        return self._get_nodes_bfs_preorder(node)

    def _get_nodes_bfs_inorder(self, node):
        """
        Retrieve the nodes using breadth-first search.
        """
        if node.left:
            self._get_nodes_bfs_preorder(node.left)
        self.nodes.append(node)
        if node.right:
            self._get_nodes_bfs_preorder(node.right)
        return self.nodes

    def get_nodes_bfs_preorder(self, node=None):
        """
        Setup retrieval of nodes using breadth-first search.
        """
        node = node if node else self.root
        return self._get_nodes_bfs_preorder(node)

    def _get_nodes_bfs_preorder(self, node):
        """
        Retrieve the nodes using breadth-first search.
        """
        self.nodes.append(node)
        if node.left:
            self._get_nodes_bfs_preorder(node.left)
        if node.right:
            self._get_nodes_bfs_preorder(node.right)
        return self.nodes

    def get_nodes_bfs_postorder(self, node=None):
        """
        Setup retrieval of nodes using breadth-first search.
        """
        node = node if node else self.root
        return self._get_nodes_bfs_postorder(self.root)

    def _get_nodes_bfs_postorder(self, node):
        """
        Retrieve the nodes using breadth-first search.
        """
        if node.left:
            self._get_nodes_bfs_postorder(node.left)
        if node.right:
            self._get_nodes_bfs_postorder(node.right)
        self.nodes.append(node)
        return self.nodes

    def is_balanced(self, threshold=1):
        """
        Returns whether the tree is within a balance threshold.
        """
        return self.get_balance() <= threshold

    def is_valid_bst(self, node=None):
        """
        Returns True if the tree starting at node is a valid binary search
        tree.
        """
        from sys import maxint as MAXINT
        MININT = -(MAXINT + 1)
        node = node if node else self.root
        return self._is_valid_bst(node, MININT, MAXINT)

    def _is_valid_bst(self, node, minint, maxint):
        """
        Determines if the tree starting at node is a valid binary search tree.
        """
        # Check if the left is valid
        left_invalid = (node.left and
                        ((node.left.value < minint) or
                          self._is_valid(node.left, minint, node.value)))
        if left_invalid: return False

        # Check if the right is invalid
        right_invalid = (node.right and
                         ((node.right.value > maxint) or
                           self._is_valid(node.right, node.value, maxint)))
        if right_invalid: return False

        return True

    def route_exists(self, node1, node2):
        """
        Returns whether a route exists between two nodes in the graph.
        """
        stack = Stack()
        for node in self.get_nodes():
            node.visited = False
        stack.push(node1)
        while not stack.is_empty():
            node = stack.pop()
            if node:
                for child in node.get_children():
                    if not child.visited:
                        if child is node2:
                            return True
                        else:
                            stack.push(child)
                node.visited = True
        return False


if __name__ == '__main__':
    tree = BinaryTree(is_bst=False)
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    tree.root = n0
    n0.left = n1
    n0.right = n2
    n1.left = n3
    n1.right = n4
    n3.left = n6
    n2.left = n5
    print tree.get_max_depth()
    print tree.get_balance()
    print tree.get_nodes_bfs_preorder(n1)
    print tree.route_exists(n0, n3)
