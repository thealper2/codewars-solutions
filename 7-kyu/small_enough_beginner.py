def small_enough(array, limit):
    return all([True if item <= limit else False for item in array])
