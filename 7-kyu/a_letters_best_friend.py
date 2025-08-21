def best_friend(txt, a, b):
    n = len(txt)
    for i in range(n):
        if txt[i] == a:
            if i == n - 1:
                return False
            
            if txt[i + 1] != b:
                return False
    
    return True
