from itertools import product


def buy_or_sell(pairs, harvested):
    actions_list = ['buy', 'sell']
    for actions in product(actions_list, repeat=3):
        current_fruit = harvested
        valid = True
        for i in range(3):
            a, b = pairs[i]
            if actions[i] == 'buy':
                if current_fruit == a:
                    current_fruit = b
                else:
                    valid = False
                    break
            else:  # sell
                if current_fruit == b:
                    current_fruit = a
                else:
                    valid = False
                    break
        if valid and current_fruit == harvested:
            return list(actions)
    return "ERROR"
