def ipv4_address_class(ipv4_addr):
    first_octet = int(ipv4_addr.split('.')[0])
    if first_octet >= 0 and first_octet <= 127:
        return 'A'
    elif first_octet >= 128 and first_octet <= 191:
        return 'B'
    elif first_octet >= 192 and first_octet <= 223:
        return 'C'
    elif first_octet >= 224 and first_octet <= 239:
        return 'D'
    elif first_octet >= 240 and first_octet <= 255:
        return 'E'
    else:
        return 'Invalid'
