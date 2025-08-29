def fair_swap(list1, list2):
    sum1 = sum(list1)
    sum2 = sum(list2)
    total = sum1 + sum2
    if total % 2 != 0:
        return set()
    
    target = total // 2
    diff = sum1 - target
    set2 = set(list2)
    result = set()
    for num in list1:
        needed = num - diff
        if needed in set2:
            result.add((num, needed))
            
    return result
