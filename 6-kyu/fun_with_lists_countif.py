def count_if(head, func):
    count = 0
    current = head
    while current is not None:
        if func(current.data):
            count += 1

        current = current.next

    return count