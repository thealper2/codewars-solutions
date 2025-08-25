class PokeScan:
    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = pkmntype
        
    def info(self):
        level_type = ''
        if self.level > 50:
            level_type = 'strong'
        elif self.level > 20:
            level_type = 'fair'
        else:
            level_type = 'weak'
            
        d = {
            'Squirtle': 'wet',
            'Charmander': 'fiery',
            'Bulbasaur': 'grassy'
        }
        
        result = f'{self.name}, a {d[self.name]} and {level_type} Pokemon.'
        return result
        
