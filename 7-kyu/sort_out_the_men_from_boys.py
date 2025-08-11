def men_from_boys(arr):
    evens = []
    odds = []
    seen = set()
    for num in arr:
        if num not in seen:
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
            
        seen.add(num)
        
    evens.sort(reverse=False)
    odds.sort(reverse=True)
    return evens + odds