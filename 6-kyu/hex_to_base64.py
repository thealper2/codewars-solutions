def hex_to_base64(hex_str: str) -> str:
    BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    bytes_data = bytes.fromhex(hex_str)
    result = []
    i = 0
    while i < len(bytes_data):
        chunk = bytes_data[i:i+3]
        value = 0
        for byte in chunk:
            value = (value << 8) | byte
            
        padding = 3 - len(chunk)
        value <<= (padding * 8)
        for j in range(4 - padding):
            index = (value >> (18 - j * 6)) & 0x3F
            result.append(BASE64_CHARS[index])
            
        result.extend(['='] * padding)
        i += 3
        
    return ''.join(result)
