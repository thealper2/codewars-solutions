def magic_sum(arr):
    result = 0
    for num in arr:
        if '3' in str(num) and num % 2 == 1:
            result += num
            
    return result