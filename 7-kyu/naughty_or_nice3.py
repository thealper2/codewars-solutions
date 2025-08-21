def naughty_or_nice(data):
    nice_count = 0
    naughty_count = 0
    for k, v in data.items():
        for k, v2 in v.items():
            if v2 == 'Nice':
                nice_count += 1
            else:
                naughty_count += 1
                
    if nice_count >= naughty_count:
        return 'Nice!'
    else:
        return 'Naughty!'
