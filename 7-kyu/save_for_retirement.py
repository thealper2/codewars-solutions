def calculate_retirement(yearly_deposit, min_target_balance):
    result = {}
    for rate in [1, 2, 3, 4, 5, 6]:
        balance = 0
        years = 0
        while balance < min_target_balance:
            years += 1
            balance += yearly_deposit
            balance *= (1 + rate / 100)
        
        result[rate] = years
        
    return result
