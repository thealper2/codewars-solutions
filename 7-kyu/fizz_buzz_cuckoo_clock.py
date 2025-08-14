def fizz_buzz_cuckoo_clock(time):
    hour_str, minute_str = time.split(':')
    hour = int(hour_str)
    minute = int(minute_str)
    
    if minute == 0:
        cuckoo_count = hour % 12
        if cuckoo_count == 0:
            cuckoo_count = 12
        return ' '.join(['Cuckoo'] * cuckoo_count)
    elif minute == 30:
        return 'Cuckoo'
    elif minute % 3 == 0 and minute % 5 == 0:
        return 'Fizz Buzz'
    elif minute % 3 == 0:
        return 'Fizz'
    elif minute % 5 == 0:
        return 'Buzz'
    else:
        return 'tick'
