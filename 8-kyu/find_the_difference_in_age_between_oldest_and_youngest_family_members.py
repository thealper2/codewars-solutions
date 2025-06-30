def difference_in_ages(ages):
    ages = list(set(ages))
    n = len(ages)
    for i in range(n):
        for j in range(n - i - 1):
            if ages[j] > ages[j + 1]:
                ages[j], ages[j + 1] = ages[j + 1], ages[j]

    return (ages[0], ages[-1], ages[-1] - ages[0])
