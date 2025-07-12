def michael_pays(cost):
    if cost < 5:
        return round(cost, 2)
    else:
        kate_contribution = min(cost / 3, 10)
        michael_payment = cost - kate_contribution
        return round(michael_payment, 2)