def black_or_white_key(key_press_count):
    pattern = 'wbwwbwbwwbwb'
    pos = (key_press_count - 1) % 88
    return 'black' if pattern[pos % 12] == 'b' else 'white'