class BullsAndCows:
    def __init__(self, secret: int):
        self.secret = str(secret)
        if len(self.secret) != 4 or len(set(self.secret)) != 4 or not self.secret.isdigit():
            raise ValueError("Secret number must be 4 distinct digits")
        self.turns = 0
        self.won = False

    def compare_with(self, guess: int) -> str:
        if self.won:
            return "You already won!"
        if self.turns >= 8:
            return "Sorry, you're out of turns!"

        guess = str(guess)
        if len(guess) != 4 or len(set(guess)) != 4 or not guess.isdigit():
            raise ValueError("Guess must be 4 distinct digits")

        self.turns += 1

        if guess == self.secret:
            self.won = True
            return "You win!"

        bulls = sum(s == g for s, g in zip(self.secret, guess))
        cows = sum(g in self.secret for g in guess) - bulls
        return f"{bulls} bull{'s' if bulls != 1 else ''} and {cows} cow{'s' if cows != 1 else ''}"
