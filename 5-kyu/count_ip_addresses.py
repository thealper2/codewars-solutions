def ips_between(start, end):
    def to_int(ip):
        a, b, c, d = map(int, ip.split('.'))
        return (a << 24) + (b << 16) + (c << 8) + d
    
    return to_int(end) - to_int(start)