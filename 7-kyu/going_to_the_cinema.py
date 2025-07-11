import math


def movie(card, ticket, perc):
    system_a_cost = 0
    system_b_cost = card
    discounted_ticket = ticket * perc
    n = 0
    
    while True:
        n += 1
        system_a_cost += ticket
        system_b_cost += discounted_ticket
        if math.ceil(system_b_cost) < system_a_cost:
            return n
        
        discounted_ticket *= perc
