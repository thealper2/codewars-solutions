def zero_plentiful(arr: list[int]) -> int:
    zeros = []
    count = 0
    arr.append(1)
    
    for item in arr:
        if item == 0:
            zeros.append(item)
        else:
            if zeros:
                if len(zeros) < 4:
                    return 0
                else:
                    count += 1
                    
            zeros = []
            
    return count