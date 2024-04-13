
import random

def guess(diff):
    secret_num = random.randint(1, 25)
    tries = 3
    print(secret_num)
    while tries > 0:
        guess_num = input("Guess the secret number 1-25: ")
        if not guess_num.isdigit():
            print("Please enter a valid number.")
            continue

        guess_num = int(guess_num)
        if guess_num != secret_num:
            print(f"{guess_num} isn't the number.")
            tries -= 1
            print(f"You have {tries} tries left.")
        else:
            return True  # Return True when the correct number is guessed
    print(f"Sorry, you've run out of tries. The correct number was {secret_num}.")
    return False  # Return False if the user runs out of tries
