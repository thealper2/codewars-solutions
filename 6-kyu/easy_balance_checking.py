import re


def balance(book):
    cleaned = re.sub(r'[^A-Za-z0-9.\s]', '', book)
    lines = [l for l in cleaned.split('\n') if l.strip()]

    original = float(lines[0])
    balance = original
    total_expense = 0.0

    result = [f"Original Balance: {original:.2f}"]

    for line in lines[1:]:
        parts = line.split()
        check_num = parts[0]
        category = parts[1]
        amount = float(parts[2])
        balance -= amount
        total_expense += amount
        result.append(f"{check_num} {category} {amount:.2f} Balance {balance:.2f}")

    avg = total_expense / (len(lines) - 1)
    result.append(f"Total expense  {total_expense:.2f}")
    result.append(f"Average expense  {avg:.2f}")

    return '\r\n'.join(result)