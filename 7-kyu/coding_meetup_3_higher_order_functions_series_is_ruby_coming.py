def is_ruby_coming(lst):
    for l in lst:
        if l["language"] == "Ruby":
            return True

    return False
