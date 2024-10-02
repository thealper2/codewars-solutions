def cookie(x):
    if type(x).__name__ == "str":
        return "Who ate the last cookie? It was Zach!"
    elif type(x).__name__ == "float" or type(x).__name__ == "int":
        return "Who ate the last cookie? It was Monica!"
    elif x == True or x == False:
        return "Who ate the last cookie? It was the dog!"
