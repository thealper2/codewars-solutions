import re


def err_bob(text):
    vowels = {"a", "e", "i", "o", "u"}

    def process_word(word):
        if not word:
            return word
        last_char = word[-1]
        if last_char.lower() not in vowels and last_char.isalpha():
            suffix = "err" if last_char.islower() else "ERR"
            return word + suffix
        return word

    tokens = re.findall(r"(\w+|\W+)", text)
    processed_tokens = []
    for token in tokens:
        if token.isalpha():
            processed_tokens.append(process_word(token))
        else:
            processed_tokens.append(token)

    return "".join(processed_tokens)
