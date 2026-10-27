def loop_size(node):
    fast = node.next.next
    slow = node.next

    while fast != slow:
        fast = fast.next.next
        slow = slow.next

    fast = fast.next
    cnt = 1
    while fast != slow:
        fast = fast.next
        cnt += 1
        
    return cnt