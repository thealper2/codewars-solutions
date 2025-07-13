def zebulans_nightmare(function):
    words = function.split("_")
    result = [words[0].lower()] + [word.capitalize() for word in words[1:]]
    return "".join(result)