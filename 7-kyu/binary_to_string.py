def binary_to_string(binary):
    binaries = binary.split('0b')
    result = ''
    for b in binaries[1:]:
        i_b = int(b, 2)
        result += chr(i_b)
        
    return result
