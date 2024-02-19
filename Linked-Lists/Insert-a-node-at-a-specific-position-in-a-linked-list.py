def insertNodeAtPosition(llist, data, position):
    new_node = SinglyLinkedListNode(data)

    if position == 0:
        new_node.next = llist
        return new_node

    current = llist
    for _ in range(position - 1):
        if current is None:
            raise Exception("Position out of bounds")
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return llist
