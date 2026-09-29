def nb_months(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    if start_price_old >= start_price_new:
        return [0, start_price_old - start_price_new]

    old_price = float(start_price_old)
    new_price = float(start_price_new)
    savings = 0.0
    percent = float(percent_loss_by_month)
    month = 0

    while True:
        month += 1
        savings += saving_per_month
        old_price *= (1 - percent / 100.0)
        new_price *= (1 - percent / 100.0)

        if month % 2 == 1:
            percent += 0.5

        available = savings + old_price - new_price
        if available >= 0:
            return [month, round(available)]