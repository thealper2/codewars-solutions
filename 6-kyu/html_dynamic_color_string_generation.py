import random

def generate_color_rgb():
    return '#' + ''.join(random.choice('0123456789ABCDEF') for _ in range(6))