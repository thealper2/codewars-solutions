def get_new_notes(salary,bills):
    total_bills = sum(bills)
    disposable_income = salary - total_bills
    if disposable_income <= 0:
        return 0
    
    return disposable_income // 5
