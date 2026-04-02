from collections import defaultdict

def calculate(price_dict,transaction):
    parsed_transaction = []
    current_digit = ''
    prices = defaultdict(list)
    total = 0
    for c in transaction:
        if c.isdigit() or c == '-':
            current_digit += c
        else:
            if current_digit:
                prices[c].append(int(current_digit))
                total += prices[c][-1] * price_dict[c]
                current_digit = ''
            else:
                if prices[c]:
                    total -= prices[c][-1] * price_dict[c]
                    prices[c].pop()
                    
    return total
