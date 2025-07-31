def amicable_numbers(num1, num2):
    def sum_proper_divisors(n):
        if n == 1:
            return 0

        divisors = {1}
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)

        return sum(divisors)

    return (
        sum_proper_divisors(num1) == num2
        and sum_proper_divisors(num2) == num1
        and num1 != num2
    )
