def dating_range(age):
    if age > 14:
        return f"{int((age / 2)) + 7}-{int((age - 7)) * 2}"
    else:
        return f"{int(age - age * 0.10)}-{int(age + age * 0.10)}"