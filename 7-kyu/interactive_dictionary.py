class Dictionary():
    def __init__(self):
        self.d = {}
        
    def newentry(self, word, definition):
        if word not in self.d:
            self.d[word] = definition
        
        return self.d[word]
        
    def look(self, key):
        return self.d.get(key, f"Can't find entry for {key}")
