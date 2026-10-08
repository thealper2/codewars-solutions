import math

class Potion:
    def __init__(self, color, volume):
        self.color = tuple(color)
        self.volume = volume

    def mix(self, other):
        total_volume = self.volume + other.volume
        new_color = []
        for i in range(3):
            mixed = (self.color[i] * self.volume + other.color[i] * other.volume) / total_volume
            new_color.append(math.ceil(mixed))

        return Potion(new_color, total_volume)