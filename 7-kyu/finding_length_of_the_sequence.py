def length_of_sequence(arr,n):
    count = 0
    first_pos = -1
    second_pos = -1
    for i in range(len(arr)):
        if arr[i] == n:
            count += 1
            if count == 1:
                first_pos = i
            
            elif count == 2:
                second_pos = i
            
            elif count > 2:
                return 0
            
    if count == 2:
        return second_pos - first_pos + 1
    else:
        return 0
