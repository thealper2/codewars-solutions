def palindrome_chain_length(n):
    k = n
    steps = 0
    while str(k) != str(k)[::-1]:
        k += int(str(k)[::-1])
        steps += 1
        
    return steps