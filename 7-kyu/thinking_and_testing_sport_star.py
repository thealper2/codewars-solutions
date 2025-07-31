def testit(actions, hurdles):
    hurdles = list(hurdles)
    hurdle_index = 0
    for action in actions:
        if hurdle_index >= len(hurdles):
            hurdle_index = 0
        current_hurdle = hurdles[hurdle_index]
        if action == "run":
            if current_hurdle == "|":
                hurdles[hurdle_index] = "/"
            elif current_hurdle == "x":
                hurdles[hurdle_index] = "/"
        elif action == "jump":
            if current_hurdle == "_":
                hurdles[hurdle_index] = "x"
            elif current_hurdle == "/":
                hurdles[hurdle_index] = "x"
        hurdle_index += 1
    return "".join(hurdles)
