def multi_table(number):
    table = []
    for i in range(1, 11):
        table.append(f"{i} * {number} = {i * number}")

    return "\n".join(table)