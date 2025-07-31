def arr2bin(arr):
    result = 0
    for item in arr:
        if type(item) != int:
            return False

        result += item

    return str(bin(result))[2:]
