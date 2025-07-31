def get_los_angeles_points(results):
    score = 0

    for result in results:
        if result[0].startswith("Los Angeles"):
            name = result[0].split()
            if len(name) != 3:
                continue

            if len(name[-1]) == 1 or name[-1].isdigit():
                continue

            if name[-1].capitalize() != name[-1]:
                continue

            if any(i.isdigit() for i in name[-1]):
                continue

            score += int(result[1].split(":")[0])

    return score
