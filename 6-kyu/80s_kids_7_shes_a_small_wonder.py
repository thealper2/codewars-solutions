class Robot:
    def __init__(self):
        self.known = {
            'thank', 'you', 'for', 'teaching', 'me',
            'i', 'already', 'know', 'the', 'word',
            'do', 'not', 'understand', 'input'
        }
        
    def learn_word(self, word):
        if not word.isalpha():
            return 'I do not understand the input'
        
        lower = word.lower()
        if lower in self.known:
            return f'I already know the word {word}'
        
        self.known.add(lower)
        return f'Thank you for teaching me {word}'