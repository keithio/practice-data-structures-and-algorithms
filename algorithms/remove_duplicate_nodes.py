def remove_duplicate_nodes(ll):
    """
    Removes duplicate nodes from a linked list.
    """
    node = ll.head
    values = set()
    prev = None

    while node:
        if node.value in values:
            prev.next = node.next
        else:
            values.append(node.value)
            prev = node
        node = node.next
