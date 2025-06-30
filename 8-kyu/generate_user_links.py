from urllib.parse import quote


def generate_link(user):
    return f"http://www.codewars.com/users/{quote(user)}"
