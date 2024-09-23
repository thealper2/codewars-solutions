def html_special_chars(data): 
    arr = []
    for i in data:
        if i == "<":
            arr.append("&lt;")
        elif i == ">":
            arr.append("&gt;")
        elif i == '"':
            arr.append("&quot;")
        elif i == "&":
            arr.append("&amp;")
        else:
            arr.append(i)

    return ''.join(arr)