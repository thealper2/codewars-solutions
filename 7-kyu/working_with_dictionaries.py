from preloaded import A001055


def inf_database(range_, str_, val):
    tmp = []
    if str_ == "equals to":
        tmp = [i for i in range(range_[0], range_[1] + 1) if A001055[i] == val]
    elif str_ == "higher than":
        tmp = [i for i in range(range_[0], range_[1] + 1) if A001055[i] > val]
    elif str_ == "lower than":
        tmp = [i for i in range(range_[0], range_[1] + 1) if A001055[i] < val]
    elif str_ == "higher and equals to":
        tmp = [i for i in range(range_[0], range_[1] + 1) if A001055[i] >= val]
    elif str_ == "lower and equals to":
        tmp = [i for i in range(range_[0], range_[1] + 1) if A001055[i] <= val]
    else:
        return "wrong constraint"

    return (len(tmp), tmp)
