import hashlib

def crack(hash_value):
    for i in range(1000000):
        pin = f"{i:05d}"
        if hashlib.md5(pin.encode()).hexdigest() == hash_value:
            return pin
        
    return None