def solution(number):
    result = [0, 0, 0]
    for i in range(1, number):
        if i % 3 == 0 and i % 5 == 0:
            result[2] += 1
        elif i % 5 == 0:
            result[1] += 1
        elif i % 3 == 0:
            result[0] += 1
            
    return result
