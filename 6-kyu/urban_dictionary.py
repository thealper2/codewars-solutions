import re


class WordDictionary:
    def __init__(self):
        self.words = {}
        
    def add_word(self, word):
        length = len(word)
        if length not in self.words:
            self.words[length] = []
            
        self.words[length].append(word)
        
    def search(self, pattern):
        length = len(pattern)
        if length not in self.words:
            return False
        
        regex_pattern = pattern.replace('.', '[a-z]')
        for word in self.words[length]:
            if re.fullmatch(regex_pattern, word):
                return True
            
        return False
