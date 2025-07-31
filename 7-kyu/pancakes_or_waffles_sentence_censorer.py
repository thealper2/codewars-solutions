def censor(text):
    censor_words = ["pancakes", "flapjacks", "slapjacks", "hotcakes"]
    highlight_words = ["waffles", "crepes", "blintzes"]
    conditional_words = ["syrup", "honey", "jam", "butter", "chocolate", "margarine"]
    text_lower = text.lower()
    has_highlight = any(word in text_lower for word in highlight_words)

    result = []
    current_word = []

    for char in text:
        if char.isalpha():
            current_word.append(char)
        else:
            if current_word:
                word = "".join(current_word)
                word_lower = word.lower()
                if word_lower in highlight_words:
                    result.append(f"**{word}**")
                elif word_lower in censor_words:
                    result.append("*" * len(word))
                elif word_lower in conditional_words:
                    if has_highlight:
                        result.append(f"**{word}**")
                    else:
                        result.append("*" * len(word))
                else:
                    result.append(word)
                current_word = []
            result.append(char)

    if current_word:
        word = "".join(current_word)
        word_lower = word.lower()
        if word_lower in highlight_words:
            result.append(f"**{word}**")
        elif word_lower in censor_words:
            result.append("*" * len(word))
        elif word_lower in conditional_words:
            if has_highlight:
                result.append(f"**{word}**")
            else:
                result.append("*" * len(word))
        else:
            result.append(word)

    return "".join(result)
