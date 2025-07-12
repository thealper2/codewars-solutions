def string_merge(string1, string2, letter):
    first_idx = second_idx = 0
    n1 = len(string1)
    n2 = len(string2)
    
    for i in range(n1):
        if string1[i] == letter:
            first_idx = i
            break
            
    for i in range(n2):
        if string2[i] == letter:
            second_idx = i
            break
            
    return string1[:first_idx] + string2[second_idx:]