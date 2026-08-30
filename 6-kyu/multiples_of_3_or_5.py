def solution(number):
    if number <= 0:
        return 0
    
    f3e = (number - 1) // 3
    f3 = 3 * f3e * (f3e + 1) // 2
    f5e = (number - 1) // 5
    f5 = 5 * f5e * (f5e + 1) // 2
    f15e = (number - 1) // 15
    f15 = 15 * f15e * (f15e + 1) // 2
    return f3 + f5 - f15
  