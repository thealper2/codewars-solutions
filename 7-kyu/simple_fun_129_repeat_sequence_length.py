def repeat_sequence_len(A):
    def F(n):
        total = 0
        while n:
            digit = n % 10
            total += digit * digit
            n //= 10
        return total
    
    if A == 0:
        return 1
    
    slow = A
    fast = A
    while True:
        slow = F(slow)
        fast = F(F(fast))
        if slow == fast:
            break
            
    cycle_length = 1
    fast = F(slow)
    while slow != fast:
        fast = F(fast)
        cycle_length += 1
    return cycle_length
