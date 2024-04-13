import requests
import random

class CurrencyGuessingGame_class:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = random.randint(1, 100)
        self.exchange_rate = self.get_exchange_rate()

    def get_exchange_rate(self):
        response = requests.get("https://v6.exchangerate-api.com/v6/3b95aa7c98abe806730e0ba9/latest/USD")
        if response.status_code == 200:
            data = response.json()
            return data['conversion_rates']['ILS']
        else:
            print("Failed to fetch exchange rates. Using default rate.")
            return 3.8  # Default rate for demonstration purposes

    def get_money_interval(self, total_value):
        lower_bound = total_value - (5 - self.difficulty)
        upper_bound = total_value + (5 - self.difficulty)
        return lower_bound, upper_bound

    def get_guess_from_user(self):
        return float(input("Enter your guess for the value in ILS: "))

    def play(self):
        print(self.secret_number)
        total_value = self.secret_number * self.exchange_rate
        lower_bound, upper_bound = self.get_money_interval(total_value)

        user_guess = self.get_guess_from_user()
        if lower_bound <= user_guess <= upper_bound:
            print(f"Congratulations! Your guess of {user_guess} ILS is within the correct interval.")
            return True
        else:
            print(f"Sorry, your guess of {user_guess} ILS is outside the correct interval, the correct is +-5 {total_value}.")
            return False


# Example usage:
#difficulty_level = 1  # Set the difficulty level here
# game = CurrencyGuessingGame_class(difficulty_level)
# result = game.play()

