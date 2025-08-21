def name_that_number(x):
    units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", 
        "eighteen", "nineteen"
    ]
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]
    
    if x < 20:
        return units[x]
    else:
        tens_digit = x // 10
        units_digit = x % 10
        if units_digit == 0:
            return tens[tens_digit]
        else:
            return tens[tens_digit] + " " + units[units_digit]
