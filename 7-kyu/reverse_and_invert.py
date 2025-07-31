def reverse_invert(lst):
    result = []
    for item in lst:
        if type(item) == int:
            item_str = str(item).replace("-", "")
            item_str = item_str[::-1]
            item_str = int(item_str)

            if item > 0:
                result.append(-item_str)
            else:
                result.append(item_str)

    return result
