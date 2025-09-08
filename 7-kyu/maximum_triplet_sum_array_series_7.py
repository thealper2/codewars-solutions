def max_tri_sum(numbers):
    set_numbers = list(set(numbers))
    n = len(set_numbers)
    max_tri = float('-inf')
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                    max_tri = max(max_tri, set_numbers[i] + set_numbers[j] + set_numbers[k])
                
    return max_tri
