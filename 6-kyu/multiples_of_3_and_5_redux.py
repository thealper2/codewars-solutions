def solution(number):
    def sum_multiples(k):
        m = (number - 1) // k
        return k * m * (m + 1) // 2

    return sum_multiples(3) + sum_multiples(5) - sum_multiples(15)