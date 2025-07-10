def encode(s:str) -> str:
    l = 0
    r = len(s) - 1
    ciphertext = ""
    while l <= r:
        if l == r:
            ciphertext += s[l]
        else:
            ciphertext += s[l]
            ciphertext += s[r]
        
        l += 1
        r -= 1
    
    return ciphertext
    
def decode(s:str) -> str:
    n = len(s)
    l = ""
    r = ""
    
    for i in range(n):
        if i % 2 == 0:
            l += s[i]
        else:
            r = s[i] + r
            
    return l + r