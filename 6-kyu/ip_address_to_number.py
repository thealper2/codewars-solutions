def ip_to_num(ip):
    octets = ip.split('.')
    result = 0
    for i in range(4):
        result += int(octets[i]) * (256 ** (3 - i))
    
    return result

def num_to_ip(num):
    result = []
    i = 4
    while i > 0:
        result.append(str(num % 256))
        num //= 256
        i -= 1
        
    return '.'.join(result[::-1])
