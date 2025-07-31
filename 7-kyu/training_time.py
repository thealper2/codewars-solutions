def shuffle_it(arr, *swaps):
    for swap in swaps:
        i, j = swap
        arr[i], arr[j] = arr[j], arr[i]
    return arr
