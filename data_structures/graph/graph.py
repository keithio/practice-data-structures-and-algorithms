class Node:
    def __init__(self, id):
        self.id = id
        self.neighbors = {}

    def __repr__(self):
        return '{0} neighboring {1}'.format(self.id, ''.join([node.id
                                            for node in self.neighbors]))

    def add_neighbor(self, node, weight=0):
        """
        Adds a neighbor node to the list of neighbors.
        """
        self.neighbors[node] = weight

    def get_connection_weight(self, neighbor):
        """
        Returns the weight of the connection between the node and a provided
        neighbor.
        """
        return self.neighbors[neighbor]

    def get_id(self):
        """
        Returns the id for the node.
        """
        return self.id

    def get_neighbors(self):
        """
        Returns the list of neighbor nodes.
        """
        return self.neighbors.keys()


class Graph:
    def __init__(self):
        self.nodes = {}
        self.num_nodes = 0

    def __contains__(self, node):
        return node in self.nodes

    def __iter__(self):
        return iter(self.nodes.values())

    def add_node(self, id):
        """
        Creates a new node and adds it to the graph.
        """
        node = Node(id)
        self.nodes[id] = node
        self.num_nodes += 1
        return node

    def get_node(self, id):
        """
        Returns a specific node in the graph as identified by its `id`. If no
        node exists with the specified `id`, return `None`.
        """
        try:
            return self.nodes[id]
        except KeyError:
            return None

    def get_nodes(self):
        """
        Returns all the nodes in the graph.
        """
        return self.nodes.keys()