def convert_my_dollars(usd, currency):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    first_char = currency[0].lower()
    conversion_rate = CONVERSION_RATES.get(currency, 0)

    if first_char not in vowels:
        conversion_rate = int(str(conversion_rate), 2)

    foreign_amount = usd * conversion_rate
    return f"You now have {foreign_amount} of {currency}."
