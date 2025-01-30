import tkinter as tk
from game import NumberGuessingGame

class GameUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")
        
        self.game = NumberGuessingGame()
        
        self.info_label = tk.Label(master, text="Guess the number between 1 and 100")
        self.info_label.pack()
        
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        self.submit_button = tk.Button(master, text="Submit Guess", command=self.submit_guess)
        self.submit_button.pack()
        
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def submit_guess(self):
        guess = int(self.entry.get())
        result = self.game.guess(guess)
        self.result_label.config(text=f"{result} - Attempts left: {self.game.get_remaining_attempts()}")
        
        if self.game.is_game_over():
            if self.game.get_remaining_attempts() == 0:
                self.result_label.config(text=f"Game Over! The correct number was {self.game.target_number}.")
            else:
                self.result_label.config(text="Congratulations! You've guessed the number.")
            self.submit_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game_ui = GameUI(root)
    root.mainloop()
