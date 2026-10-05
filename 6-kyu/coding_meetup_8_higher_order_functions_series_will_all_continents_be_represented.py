def all_continents(lst): 
    required = {'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'}
    continents = {developer['continent'] for developer in lst}
    return required.issubset(continents)