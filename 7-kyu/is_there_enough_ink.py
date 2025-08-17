def enough_ink(image, r, g, b):
    need_r, need_g, need_b = 0, 0, 0
    for row in image:
        for pixel in row:
            red = int(pixel[0:2], 16)
            green = int(pixel[2:4], 16)
            blue = int(pixel[4:6], 16)
            need_r += 255 - red
            need_g += 255 - green
            need_b += 255 - blue
            
    if need_r > r or need_g > g or need_b > b:
        return False
    
    return True
