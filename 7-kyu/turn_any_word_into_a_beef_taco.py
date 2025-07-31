def tacofy(word):
    taco_ingredients = ["shell"]
    lower_word = word.lower()
    for char in lower_word:
        if char in {"a", "e", "i", "o", "u"}:
            taco_ingredients.append("beef")
        elif char == "t":
            taco_ingredients.append("tomato")
        elif char == "l":
            taco_ingredients.append("lettuce")
        elif char == "c":
            taco_ingredients.append("cheese")
        elif char == "g":
            taco_ingredients.append("guacamole")
        elif char == "s":
            taco_ingredients.append("salsa")

    taco_ingredients.append("shell")
    return taco_ingredients
