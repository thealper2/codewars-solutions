def get_turkish_number(num):
    turkish_digits = {
        0: "sıfır",
        1: "bir",
        2: "iki",
        3: "üç",
        4: "dört",
        5: "beş",
        6: "altı",
        7: "yedi",
        8: "sekiz",
        9: "dokuz",
        10: "on",
        20: "yirmi",
        30: "otuz",
        40: "kırk",
        50: "elli",
        60: "altmış",
        70: "yetmiş",
        80: "seksen",
        90: "doksan",
    }

    if num < 10 or num % 10 == 0:
        return turkish_digits[num]

    return turkish_digits[10 * (num // 10)] + " " + turkish_digits[num % 10]
