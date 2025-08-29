from preloaded import display


def hex_to_bitmap(hex_str: str) -> str:
    lines = []
    n = len(hex_str)
    
    for i in range(0, n, 2):
        byte = hex_str[i:i+2]
        num = int(byte, 16)
        binary = bin(num)[2:].zfill(8)
        lines.append(binary)
    
    return '\n'.join(lines)
    
detailed_errors = True
