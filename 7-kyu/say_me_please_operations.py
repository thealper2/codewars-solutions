def say_me_operations(string_numbers):
    numbers = list(map(int, string_numbers.split()))
    operations = []

    for i in range(2, len(numbers)):
        first = numbers[i - 2]
        second = numbers[i - 1]
        current = numbers[i]

        if first + second == current:
            operations.append("addition")
        elif first - second == current:
            operations.append("subtraction")
        elif first * second == current:
            operations.append("multiplication")
        elif second != 0 and first // second == current:
            operations.append("division")
        else:
            operations.append("unknown")

    return ", ".join(operations)
