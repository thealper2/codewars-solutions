class MarioAdapter:
    def __init__(self, mario):
        self.mario = mario

    def attack(self, target):
        damage = self.mario.jump_attack()
        target.health -= damage
