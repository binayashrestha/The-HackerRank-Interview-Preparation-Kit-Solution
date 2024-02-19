def sortedInsert(llist, data):
    node = DoublyLinkedListNode(data)
    if llist is None:  # checking if the list is empty
        return node
    elif data <= llist.data:  # this finds the correct position for insertion
        node.next = llist
        llist.prev = node
        return node
    else:
        node = sortedInsert(
            llist.next, data
        )  # make a recursive call to sortedInsert function
        llist.next = node
        node.prev = llist
        return llist
