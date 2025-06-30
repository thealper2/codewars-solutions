def validate(username, password):
    if "\\" in password or "\|" in password:
        return "Wrong username or password!"

    database = Database()
    return database.login(username, password)
