def my_first_kata(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return False
    return a % b + b % a
