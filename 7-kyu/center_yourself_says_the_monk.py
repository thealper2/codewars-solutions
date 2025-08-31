def center(strng, width, fill=' '):
    if len(strng) >= width:
        return strng
    
    width -= len(strng)
    m = ((width + 1) // 2)
    return fill * m + strng + fill * (width - m)
