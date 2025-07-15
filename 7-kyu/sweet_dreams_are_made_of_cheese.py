import math


def pay_cheese(arr):
    total_wheels = sum(arr)
    total_minutes = total_wheels * 6 / 10
    total_hours = math.ceil(total_minutes / 60)
    total_wages_pence = total_hours * 4 * 875
    total_pounds = total_wages_pence // 100
    total_pence = total_wages_pence % 100
    return f"L{total_pounds}"
