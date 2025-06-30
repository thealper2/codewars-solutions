def flick_switch(arr):
    found = True
    result = []
    for word in arr:
        if word == "flick":
            found = not found

        result.append(found)

    return result
