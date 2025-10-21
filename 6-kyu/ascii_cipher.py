def largest_prime(n):
    if n < 2:
        return None
    
    factor = n
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factor = n
            n //= i
            
    if n > 1:
        factor = n
        
    return factor

def ascii_cipher(message, key):
    prime = largest_prime(abs(key))
    if key < 0:
        prime = -prime
        
    result = []
    for c in message:
        new_val = (ord(c) + prime) % 128
        result.append(chr(new_val))
        
    return ''.join(result)
