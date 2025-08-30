def digits(num):
    str_num = str(num)
    result = []
    n = len(str_num)
    
    for i in range(n):
        for j in range(i + 1, n):
            result.append(int(str_num[i]) + int(str_num[j]))
            
    return result
