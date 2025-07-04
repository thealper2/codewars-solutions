def computer_to_phone(numbers):
    result = ""
    for number in numbers:
        if number == "0":
            result += number
        elif int(number) > 6:
            result += str(int(number) - 6)
        elif int(number) < 4:
            result += str(int(number) + 6)
        else:
            result += number
        
    return result
