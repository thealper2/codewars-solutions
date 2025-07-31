from collections import defaultdict


def strange_coach(players):
    letter_counts = defaultdict(int)
    for surname in players:
        if surname:
            first_letter = surname[0].lower()
            letter_counts[first_letter] += 1

    possible_letters = [letter for letter, count in letter_counts.items() if count >= 5]
    possible_letters.sort()

    if not possible_letters:
        return "forfeit"
    else:
        return "".join(possible_letters)
