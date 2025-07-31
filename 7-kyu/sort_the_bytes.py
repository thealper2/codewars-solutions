def sort_bytes(n):
    byte1 = (n >> 24) & 0xFF
    byte2 = (n >> 16) & 0xFF
    byte3 = (n >> 8) & 0xFF
    byte4 = n & 0xFF
    bytes_list = [byte1, byte2, byte3, byte4]
    bytes_list.sort(reverse=True)
    new_number = (
        (bytes_list[0] << 24)
        | (bytes_list[1] << 16)
        | (bytes_list[2] << 8)
        | bytes_list[3]
    )
    return new_number
