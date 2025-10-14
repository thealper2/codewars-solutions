def sequence_classifier(arr):
    n = len(arr)
    
    if all(arr[i] == arr[0] for i in range(1, n)):
        return 5
    
    strictly_increasing = True
    strictly_decreasing = True
    not_increasing = True
    not_decreasing = True
    
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            strictly_decreasing = False
            not_increasing = False
            
        elif arr[i] < arr[i - 1]:
            strictly_increasing = False
            not_decreasing = False
            
        else:
            strictly_increasing = False
            strictly_decreasing = False
            
    if strictly_increasing:
        return 1
    elif not_decreasing:
        return 2
    elif strictly_decreasing:
        return 3
    elif not_increasing:
        return 4
    else:
        return 0
