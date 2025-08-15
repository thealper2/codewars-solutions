def move_ten(st):
    return ''.join([chr((ord(c) - ord('a') + 10) % 26 + ord('a')) for c in st])
