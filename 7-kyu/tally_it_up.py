def score_to_tally(score):
    letters = ['a', 'b', 'c', 'd', 'e']
    a = score // 5
    b = score % 5
    result = ''.join(['e <br>' for _ in range(a)])
    if b:
        result += letters[b - 1]
        
    return result
