def number_of_clans(divisors, k):
    clans = set()
    for num in range(1, k + 1):
        signature = tuple(num % d == 0 for d in divisors)
        clans.add(signature)
    return len(clans)
