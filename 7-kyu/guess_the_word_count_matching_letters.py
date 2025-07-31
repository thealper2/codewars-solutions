def count_correct_characters(correct, guess):
    if len(correct) != len(guess):
        raise Error()

    return sum(1 if a == b else 0 for a, b in zip(correct, guess))
