def guess_the_card(audience):
    DECK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
    for _ in range(3):
        columns = [DECK[i::3] for i in range(3)]
        col_index = audience.get_input(columns)
        DECK = columns[(col_index + 1) % 3] + columns[col_index] + columns[(col_index + 2) % 3]
        
    return DECK[10]
