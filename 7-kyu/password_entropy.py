import math

def entropy(password):
    lowercase = set('abcdefghijklmnopqrstuvwxyz')
    uppercase = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    digits = set('0123456789')
    special = set('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')
    
    pool_size = 0
    used_pools = 0
    
    if any(c in lowercase for c in password):
        pool_size += 26
        used_pools += 1
    
    if any(c in uppercase for c in password):
        pool_size += 26
        used_pools += 1
    
    if any(c in digits for c in password):
        pool_size += 10
        used_pools += 1
    
    if any(c in special for c in password):
        pool_size += 32
        used_pools += 1
    
    if pool_size == 0:
        return 0.0
    
    L = len(password)
    E = L * math.log2(pool_size)
    
    return E
