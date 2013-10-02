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

    def delete_node(self, node):
        if node and node.next:
            next = node.next
            node.value = next.value
            node.next = next.next

    def distinct(self):
        if not self.head:
            return None

        node = self.head
        values = set()
        while node:
            if node.value in values:
                node = node.next
            else:
                values.append(node.value)

    def next(self):
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

    def __iter__(self):
        return self


if __name__ == '__main__':
    ll = LinkedList()
    for i in range(1, 6):
        ll.append(i)
    for n in ll:
        print n
    for n in ll:
        ll.pop(n)
    for i in range(1, 6):
        ll.push(i)
    for n in ll:
        print n
