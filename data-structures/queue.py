class Node:
    """
    A node is an object that may be contained in the queue defined below.
    """
    def __init__(self, value):
        """
        Initialize the node with a provided value.
        """
        self.value = value
        self.next = None


class Queue:
    """
    A queue is an abstract data type that acts as a container for nodes
    (objects) that are inserted and removed according to first-in-first-out.
    """
    def __init__(self):
        self.first = None
        self.last = None

    def dequeue(self):
        """
        Remove the node at the front of the queue and return its value.

        Raise an exception if the queue is empty.
        """
        if self.front:
            value = self.first.value
            self.first = self.first.next
            return value
        raise Exception('Queue is empty, cannot dequeue.')

    def enqueue(self, value):
        """
        Insert a node with a value at the end of the queue.
        """
        node = Node(value)
        if self.first:
            self.last.next = node
            self.last = node
        else:
            self.first = node
            self.last = node
        return True

    def is_empty(self):
        """
        Returns whether the queue is empty.
        """
        return bool(self.first)

    def size(self):
        """
        Returns the size of the queue.
        """
        node = self.first
        num_nodes = 0
        while node.next:
            num_nodes += 1
            node = node.next
        return num_nodes
