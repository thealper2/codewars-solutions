def bingo(array): 
    chars = ['B', 'I', 'N', 'G', 'O']
    for num in array:
        char = chr(num + ord('A') - 1)
        if char in chars:
            chars.remove(char)
            
    if chars:
        return "LOSE"
    else:
        return "WIN"
