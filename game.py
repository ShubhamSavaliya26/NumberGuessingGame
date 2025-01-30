import random

class NumberGuessingGame:
    def __init__(self, min_number=1, max_number=100, max_attempts=10):
        self.min_number = min_number
        self.max_number = max_number
        self.max_attempts = max_attempts
        self.target_number = random.randint(min_number, max_number)
        self.attempts_left = max_attempts
        self.guesses = []

    def guess(self, player_guess):
        self.guesses.append(player_guess)
        self.attempts_left -= 1

        if player_guess < self.target_number:
            return "Too low!"
        elif player_guess > self.target_number:
            return "Too high!"
        else:
            return "Correct!"

    def is_game_over(self):
        return self.attempts_left == 0 or self.target_number in self.guesses

    def get_remaining_attempts(self):
        return self.attempts_left

    def get_high_score(self):
        # Implement logic for getting high score from the database
        pass

