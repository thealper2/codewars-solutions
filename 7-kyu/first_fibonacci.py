def solution(first, second):
    while first >= 0 and second >= first:
        first, second = second - first, first
    
    return (second, first + second)
