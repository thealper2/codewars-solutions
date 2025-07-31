def count_loop_iterations(arr):
    evaluations = []
    product = 1
    for v, inclusive in arr:
        if inclusive:
            current = v + 2
        else:
            current = v + 1
        evaluations.append(product * current)
        product *= current - 1

    return evaluations
