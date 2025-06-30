def logical_calc(array, op):
    result = array[0]

    for i in range(1, len(array)):
        if op == "AND":
            result = result & array[i]
        elif op == "OR":
            result = result | array[i]
        elif op == "XOR":
            result = result ^ array[i]

    return result
