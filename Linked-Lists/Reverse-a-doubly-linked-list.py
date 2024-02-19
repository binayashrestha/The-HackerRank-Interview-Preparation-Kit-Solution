def reverse(llist):
    if not llist:  # check for empty list
        return None

    current = llist
    while current:
        current.next, current.prev = current.prev, current.next  # swap
        if not current.prev:
            return current
        current = current.prev
