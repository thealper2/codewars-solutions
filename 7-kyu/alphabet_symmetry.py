def solve(strings: list[str]) -> list[int]:
    result = []
    for word in strings:
        count = 0
        for index, char in enumerate(word.lower(), start=1):
            if ord(char) - ord("a") + 1 == index:
                count += 1

        result.append(count)
    return result
