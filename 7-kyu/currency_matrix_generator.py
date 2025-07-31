def generate_currency_matrix(currency):
    currency_strength = ["EUR", "GBP", "AUD", "NZD", "USD", "CAD", "CHF", "JPY"]
    n = len(currency_strength)
    result = []
    found = False

    for i in range(n):
        if currency_strength[i] == currency:
            found = True

        elif found:
            result.append(currency + currency_strength[i])

        else:
            result.append(currency_strength[i] + currency)

    return result
