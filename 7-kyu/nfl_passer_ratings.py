def passer_rating(att, yds, comp, td, ints):
    def get_bounded(x):
        return max(0, min(x, 2.375))
    
    A = ((comp / att) - 0.3) * 5
    B = ((yds / att) - 3) * 0.25
    C = (td / att) * 20
    D = 2.375 - ((ints / att) * 25)
    A = get_bounded(A)
    B = get_bounded(B)
    C = get_bounded(C)
    D = get_bounded(D)
    rating = ((A + B + C + D) / 6) * 100
    return round(rating, 1)
