def to_bytes(n):
    if n == 0:
        return ['00000000']
    
    bytes_list = []
    while n:
        byte = n & 0xFF
        bytes_list.append(bin(byte)[2:].zfill(8))
        n >>= 8
        
    return bytes_list[::-1]
