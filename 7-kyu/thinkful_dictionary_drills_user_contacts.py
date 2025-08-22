def user_contacts(data):
    users = {}
    for row in data:
        if row:
            if len(row) == 1:
                users[row[0]] = None
            else:
                users[row[0]] = row[1]
                
    return users
