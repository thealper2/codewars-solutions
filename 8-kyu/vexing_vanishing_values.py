def mul_by_n(lst, n):
    print("Inputs: ", lst, n)
    result = [x * n for x in lst]
    print("Result: ", list(result))
    return list(result)