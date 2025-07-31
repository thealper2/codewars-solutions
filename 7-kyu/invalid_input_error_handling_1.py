def get_count(words=""):
    result = {"vowels": 0, "consonants": 0}
    if not words:
        return result

    if type(words) == str:
        for c in words:
            if c == " ":
                continue
            elif c.lower() in "aeiou":
                result["vowels"] += 1
            elif not c.isdigit() and c.isalpha():
                result["consonants"] += 1

    return result
