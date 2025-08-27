def count_wins(winners_list, country):
    count = 0
    for winner in winners_list:
        if winner['country'] == country:
            count += 1
            
    return count
