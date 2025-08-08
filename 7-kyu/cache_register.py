def register_transaction(n):
    if not hasattr(register_transaction, "transactions"):
        register_transaction.transactions = []

    formatted = "${:,.2f}".format(round(n, 2))
    register_transaction.transactions.append(formatted)
    return register_transaction.transactions.copy()
