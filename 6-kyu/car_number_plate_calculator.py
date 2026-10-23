def find_the_number_plate(customer_id):
    series_index = customer_id // 999
    serial = customer_id % 999 + 1
    l = series_index % 26
    m = (series_index // 26) % 26
    r = (series_index // (26 * 26)) % 26
    letters = chr(ord('a') + l) + chr(ord('a') + m) + chr(ord('a') + r)
    return f"{letters}{serial:03d}"