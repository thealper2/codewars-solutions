class HighScoreTable:
    def __init__(self, size):
        self.scores = []
        self.size = size

    def update(self, score):
        self.scores.append(score)
        self.scores.sort(reverse=True)
        self.scores = self.scores[:self.size]

    def reset(self):
        self.scores = []