def numbers_of_letters(n):
    digits = ['zero', 'one', 'two', 'three', 'four',
              'five', 'six', 'seven', 'eight', 'nine']
    
    def to_words(num):
        return ''.join(digits[int(d)] for d in str(num))
    
    result = []
    current = n
    while True:
        word = to_words(current)
        result.append(word)
        if len(word) == current:
            break
            
        current = len(word)
        
    return result