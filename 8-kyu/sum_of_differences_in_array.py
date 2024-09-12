def sum_of_differences(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    c = 0
    for i in range(len(arr) - 1):
        c += arr[i] - arr[i+1]
    
    return c

print(sum_of_differences([1, 2, 10]))
print(sum_of_differences([-3, -2, -1]))
print(sum_of_differences([1, 1, 1, 1, 1]))
print(sum_of_differences([]))