def count_deaf_rats(town):
    answer = 0

    pied_piper = ""

    for char in town:
        if char != " ":
            pied_piper += char

    position = pied_piper.index("P")
    position_p = position

    position += 1

    my_rats = []

    for i in range(position, len(pied_piper), 2):
        rats = pied_piper[i:i + 2]
        my_rats.append(rats)

    for rat in my_rats:
        if rat == "~O":
            answer += 1

    my_rats.clear()

    if position_p != 0:
        for i in range(0, position_p, 2):
            rats = pied_piper[i:i + 2]
            my_rats.append(rats)

        for rat in my_rats:
            if rat == "O~":
                answer += 1

    return answer