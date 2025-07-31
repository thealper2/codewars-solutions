def queue(queuers, pos):
    time = 0

    while True:
        current = queuers.pop(0)
        time += 1
        current -= 1

        if pos == 0:
            if current == 0:
                return time
            else:
                queuers.append(current)
                pos = len(queuers) - 1
        else:
            if current > 0:
                queuers.append(current)

            pos -= 1
