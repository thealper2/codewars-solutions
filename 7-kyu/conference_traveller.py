def conference_picker(cities_visited, cities_offered):
    for city in cities_offered:
        if city in cities_visited:
            continue
        else:
            return city

    return "No worthwhile conferences this year!"
