import re


def abbreviate(s):
    def repl(m):
        word = m.group(0)
        if len(word) < 4:
            return word

        return word[0] + str(len(word) - 2) + word[-1]

    return re.sub(r'[A-Za-z]+', repl, s)