def locker_run(lockers):
    result = []
    i = 1
    while i ** 2 <= lockers:
        result.append(i ** 2)
        i += 1
        
    return result
