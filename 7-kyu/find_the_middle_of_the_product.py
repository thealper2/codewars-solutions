def find_middle(s):
    if not isinstance(s, str):
        return -1

    digits = []
    for char in s:
        if char.isdigit():
            digits.append(int(char))

    if not digits:
        return -1

    product = 1
    for num in digits:
        product *= num

    product_str = str(product)
    length = len(product_str)

    if length == 0:
        return -1

    if length % 2 == 1:
        middle_index = length // 2
        return int(product_str[middle_index])
    else:
        middle_start = (length // 2) - 1
        middle_two = product_str[middle_start : middle_start + 2]
        if middle_two[0] == "0":
            middle_two = middle_two.lstrip("0")
            if not middle_two:
                return 0
        return int(middle_two)
