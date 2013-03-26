from stack import Stack


class TreeNode:
    """
    Defines a node for the binary tree.
    """
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

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

    def is_leaf(self):
        return self.left is not None and self.right is not None

    def is_root(self):
        return self.parent is None

    def __repr__(self):
        return '{}'.format(self.value)


class BinaryTree:
    """
    Defines a binary tree, or a tree in which each node can have at most two
    child nodes.
    """
    def __init__(self):
        self.root = None
        self.nodes = []

    def get_balance(self):
        """
        Returns the balance of the tree, or the difference between the max
        depth and the min depth.
        """
        return self.get_max_depth() - self.get_min_depth()

    def get_max_depth(self, node=None, initial=1):
        """
        Recursively calculates the max depth of the tree.
        """
        if not node:
            if not self.root:
                return 0
            else:
                if initial:
                    node = self.root
                else:
                    return 0
        return 1 + max(self.get_max_depth(node.left, 0),
                       self.get_max_depth(node.right, 0))

    def get_min_depth(self, node=None, initial=1):
        """
        Recursively calculates the min depth of the tree.
        """
        if not node:
            if not self.root:
                return 0
            else:
                if initial:
                    node = self.root
                else:
                    return 0
        return 1 + min(self.get_min_depth(node.left, 0),
                       self.get_min_depth(node.right, 0))

    def is_balanced(self, threshold=1):
        """
        Returns whether the tree is within a balance threshold.
        """
        return self.get_balance() <= threshold

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

    def get_nodes(self, node=None):
        if not node:
            node = self.root
        return self.get_nodes_bfs_preorder(node, initial=1)

    def get_nodes_bfs_preorder(self, node=None, initial=0):
        """
        Traverse the tree in order.
        """
        if not node:
            if initial:
                node = self.root
            else:
                return None
        self.nodes.append(node)
        if node.left:
            self.get_nodes_bfs_preorder(node.left)
        if node.right:
            self.get_nodes_bfs_preorder(node.right)
        return self.nodes


if __name__ == '__main__':
    tree = BinaryTree()
    n0 = TreeNode(0)
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
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
