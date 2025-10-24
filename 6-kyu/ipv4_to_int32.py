def ip_to_int32(ip):
    octets = ip.split('.')
    result = 0
    for i, octet in enumerate(octets):
        result += int(octet) << (8 * (3 - i))
        
    return result
