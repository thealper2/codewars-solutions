def last_man_standing(n):
    numbers = [_ for _ in range(1, n + 1)]
    left = True
    while len(numbers) > 1:
        if left:
            numbers = numbers[1::2]
        else:
            numbers = numbers[-2::-2][::-1]
        
        left = not left
        
    return numbers[0]
