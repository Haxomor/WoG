import random

secret_num = random.randint(1, 100)
tries = 3

class guess_class:
    def guess(diff):
        global tries
        while tries > 0:

            difficulty = input(f"Guess the secret number: ")
            if int(difficulty) != secret_num:
                print(f"{difficulty} isn't the number.")
                tries -= 1
                print(f"You have {tries} tries left.")
            else:
                print("Congratulations! You guessed the correct number.")
                break
        else:
            print(f"Sorry, you've run out of tries. The correct number was {secret_num}.")
