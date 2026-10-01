def up_array(arr):
    if not arr:
        return None

    for x in arr:
        if x < 0 or x > 9:
            return None

    result = arr[:]
    carry = 1
    for i in range(len(result) - 1, -1, -1):
        if carry == 0:
            break
        s = result[i] + carry
        result[i] = s % 10
        carry = s // 10

    if carry:
        result.insert(0, 1)
    return result