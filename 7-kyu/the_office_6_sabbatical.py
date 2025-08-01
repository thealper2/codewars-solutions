def sabb(s, val, happiness):
    sabbatical_letters = {'s', 'a', 'b', 't', 'i', 'c', 'l'}
    count = 0
    for char in s.lower():
        if char in sabbatical_letters:
            count += 1
    total = val + happiness + count
    if total > 22:
        return 'Sabbatical! Boom!'
    else:
        return 'Back to your desk, boy.'
