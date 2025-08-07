def get_nice_names(people):
    return [k['name'] for k in people if k['was_nice']]

def get_naughty_names(people):
    return [k['name'] for k in people if not k['was_nice']]
