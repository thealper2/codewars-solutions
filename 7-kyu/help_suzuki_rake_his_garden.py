def rake_garden(garden):
    items = garden.split()
    result = []
    for item in items:
        if item == "rock" or item == "gravel":
            result.append(item)
        else:
            result.append("gravel")

    return " ".join(result)
