class BatmanQuotes(object):

    @staticmethod
    def get_quote(quotes, hero):
        digit = None
        digit_pos = -1
        for i, char in enumerate(hero):
            if char.isdigit():
                digit = int(char)
                digit_pos = i
                break

        original_names = ["Batman", "Robin", "Joker"]
        possible_names = []
        for original in original_names:
            if len(original) == len(hero):
                possible_names.append(original)

        correct_name = None
        for candidate in possible_names:
            match = True
            for i in range(len(hero)):
                if i == digit_pos:
                    continue
                if hero[i] != candidate[i]:
                    match = False
                    break
            if match:
                correct_name = candidate
                break

        quote = quotes[digit]
        return f"{correct_name}: {quote}"