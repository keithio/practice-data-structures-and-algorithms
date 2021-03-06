class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.curr = None
        self.head = None

    def __iter__(self):
        return self

    def __len__(self):
        if not self.head:
            return
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def append(self, value):
        """
        Add a new node at the end of the linked list.
        """
        node = Node(value)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
        else:
            self.head = node

    def distinct(self):
        """
        Return a list of nodes without duplicates.
        """
        if not self.head:
            return None

        node = self.head
        values = []
        while node:
            if node.value in values:
                node = node.next
            else:
                values.append(node.value)
        return values

    def get_head(self):
        """
        Returns the first node in the linked list.
        """
        return self.head

    def get_tail(self):
        """
        Returns the last node in the linked list.
        """
        last_node = self.head
        while last_node.next:
            if last_node.next:
                last_node = last_node.next
        return last_node

    def has_cycle(self):
        """
        Check if the linked list has a cycle.
        """
        fast = self.head
        slow = self.head
        while True:
            slow = slow.next
            if not fast.next:
                # Reached the end, therefore no cycle
                return False
            else:
                # Otherwise, continue moving at double speed
                fast = fast.next.next
            if not slow or not fast:
                # Both are non-existent, therefore no cycle
                return False
            if fast is slow:
                # Both point to the same node, therefore cycle
                return True

    def next(self):
        """
        Get the next node in the linked list.
        """
        if self.head and not self.curr:
            self.curr = self.head
            return self.curr
        elif self.curr.next:
            self.curr = self.curr.next
            return self.curr
        else:
            raise StopIteration

    def pop(self):
        """
        Removes the first node from the linked list and returns its value.
        """
        node = self.head
        value = node.value
        self.head = node.next
        del(node)
        return value

    def push(self, value):
        """
        Add a new node at the beginning of the linked list.
        """
        node = Node(value)
        node.next = self.head
        self.head = node

    def remove(self, node):
        """
        Removes a specified node and updates the linked list.
        """
        if node and node.next:
            next = node.next
            node.value = next.value
            node.next = next.next
