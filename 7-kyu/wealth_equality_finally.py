def redistribute_wealth(wealth):
    avg = sum(wealth) / len(wealth)
    for i in range(len(wealth)):
        wealth[i] = avg
