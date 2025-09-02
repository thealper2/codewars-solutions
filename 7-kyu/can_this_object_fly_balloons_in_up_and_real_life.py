class Journey:
    def __init__(self, obj, crew, balloons):
        self.obj = obj
        self.crew = crew
        self.balloons = balloons
        
    def isPossible(self):
        total_weight = self.obj['weight'] + self.crew * 80
        lift = self.balloons * 4.8 / 1000
        return lift >= total_weight
