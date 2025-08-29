def who_took_the_car_key(message):
    return ''.join([chr(int(m, 2)) for m in message])
