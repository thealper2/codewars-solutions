class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.listeners = set()
        
    def how_many(self, people):
        new_listeners = 0
        for person in people:
            lower_name = person.lower()
            if lower_name not in self.listeners:
                new_listeners += 1
                self.listeners.add(lower_name)
                
        return new_listeners
