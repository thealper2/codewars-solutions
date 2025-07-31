def format_poem(poem):
    return ".\n".join([s.strip() for s in poem.split(". ")])
