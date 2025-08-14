import math


def sum_average(arr):
    total_sum = 0.0
    for subarray in arr:
        if len(subarray) == 0:
            continue
            
        average = sum(subarray) / len(subarray)
        total_sum += average
    
    return math.floor(total_sum)
