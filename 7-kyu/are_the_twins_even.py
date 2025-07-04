def even_twins(numbers):
    n = len(numbers)
    seen = []
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            s = numbers[i] + numbers[j]
            if s % 2 == 0 and s not in seen:
                count += 1
                seen.append(s)
    
    return count
