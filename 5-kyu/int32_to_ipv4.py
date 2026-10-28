def int32_to_ip(n):
    octet1 = (n // 16777216) % 256
    octet2 = (n // 65536) % 256
    octet3 = (n // 256) % 256
    octet4 = n % 256
    return f"{octet1}.{octet2}.{octet3}.{octet4}"