# linked_list.py

This is a custom implementation of a linked list in Python that does not use
any built-in data structures. A linked list is a simple data structure that
is represented by a collection of nodes in which each node has a pointer to
the next node. The last node can either have a pointer to null, or maintain a
"sentinal node" that represents the end. A linked list can either be singly
linked or doubly linked. A doubly linked list has a pointer to the previous
node in addition to the next node. Linked lists have an insertion time of
O(1) and a lookup time of O(n).

In Python, the ``dict`` data structure can be used as it has many of the same
methods, e.g. ``list.append()``, ``list.extend()``, ``list.insert()``,
``list.remove()``, ``list.pop()``, ``list.index()``, ``list.count()``, and so
on.