def validate_hello(greetings):
    greeting = ["hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"]
    for g in greeting:
        if g in greetings.lower():
            return True

    return False
