class Node:
    """
    A node is an object that may be contained in the stack defined below.
    """
    def __init__(self, value):
        """
        Initialize the node with a provided value.
        """
        self.value = value
        self.next = None


class Stack:
    """
    A stack is an abstract data type that acts as a container for nodes
    (objects) that are inserted and removed according to last-in-first-out.
    """
    def __init__(self):
        """
        Initialize the stack.
        """
        self.top = None

    def is_empty(self):
        """
        Returns whether or not the stack is empty.
        """
        return bool(self.top)

    def pop(self):
        """
        Removes the node at the top of the stack and returns its value.
        """
        node = self.top
        self.top = node.next
        return node.value

    def push(self, value):
        """
        Add a new node with a given value to the top of the stack.
        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def size(self):
        """
        Returns the number of nodes in the stack.
        """
        node = self.top
        num_nodes = 0
        while node.next:
            num_nodes += 1
            node = node.next
        return num_nodes

    def get_top(self):
        """
        Returns the value of the top node without removing it.
        """
        return self.top.value
