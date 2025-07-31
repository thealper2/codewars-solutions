def each_char(string, arg):
    n = len(string)
    result = ""

    for i in range(n):
        if type(arg) == str:
            result += string[i]
            result += arg
        else:
            result += arg(string[i])

    return result
