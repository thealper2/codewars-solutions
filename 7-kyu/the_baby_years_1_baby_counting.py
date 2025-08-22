def baby_count(x):
    s = x.lower()
    count = 0
    while True:
        for char in 'baby':
            if char in s:
                s = s.replace(char, '', 1)
            else:
                return count if count > 0 else "Where's the baby?!"
        count += 1
