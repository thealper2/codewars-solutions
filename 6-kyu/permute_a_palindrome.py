def permute_a_palindrome(input): 
    odd = 0
    seen = {}
    for c in input:
        seen[c] = seen.get(c, 0) + 1
        
    for v in seen.values():
        if v % 2:
            odd += 1
            if odd > 1:
                return False
    
    return True