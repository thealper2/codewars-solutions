def how_many_times(annual_price, individual_price):
    count = 1

    while annual_price > individual_price:
        count += 1
        annual_price -= individual_price

    return count
