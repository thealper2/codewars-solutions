import re

def ipv4_address(address):
    octet = r'(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)'
    regex_pattern = f'{octet}\\.{octet}\\.{octet}\\.{octet}'
    return True if re.fullmatch(regex_pattern, address) else False