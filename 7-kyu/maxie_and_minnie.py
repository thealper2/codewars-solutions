def swap(n):
    digits = list(str(n))
    
    maxie = n
    minnie = n

    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            digits[i], digits[j] = digits[j], digits[i]

            if digits[0] != '0':
                number = int(''.join(digits))

                maxie = max(maxie, number)
                minnie = min(minnie, number)

            digits[i], digits[j] = digits[j], digits[i]

    return maxie, minnie
