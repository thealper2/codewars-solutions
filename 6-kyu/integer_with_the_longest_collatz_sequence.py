def longest_collatz(arr):
    best_collatz = None
    best_counter = 0
    for i, n in enumerate(arr):
        counter = 0
        num = arr[i]
        while num != 1:
            if num % 2 == 1:
                num = 3 * num + 1
            else:
                num = num / 2
                
            counter += 1
            
        if counter > best_counter:
            best_collatz = n
            best_counter = counter
            
    return best_collatz