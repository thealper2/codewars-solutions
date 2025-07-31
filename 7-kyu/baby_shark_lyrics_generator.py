def baby_shark_lyrics():
    titles = ["Baby", "Mommy", "Daddy", "Grandma", "Grandpa"]
    verses = [
        f"{title} shark, doo doo doo doo doo doo\n" * 3 + f"{title} shark!\n"
        for title in titles
    ]
    return (
        "".join(verses)
        + "Let's go hunt, doo doo doo doo doo doo\n" * 3
        + "Let's go hunt!\nRun away,…"
    )
