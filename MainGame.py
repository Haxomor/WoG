import MemoryGame
import CurrencyRouletteGame
import GuessGame

name = input("Welcome, what is your name? ")
print(f"Hello {name} and welcome to the World of Games")

print("This is all our games:")
print(" 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n",
      "2. Guess Game - guess a number and see if you chose like the computer \n",
      "3. Currency Roulette - try and guess the value of a random amount of USD in ILS \n")
game_num = input("Please choose a game to play: ")
game_diff = input("Please choose game difficulty from 1 to 5: ")
def congr():
    diff = MainGame.load_game()
    result = MemoryGame.play(diff)
    if result:
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost.")
def load_game(num, diff):

    if game_num == "1":
        print(f"You chose the Memory Game with difficulty of {diff}, good luck!")
        MemoryGame.generate_sequence(diff)
        MemoryGame.get_list_from_user(diff)
        #MemoryGame.is_list_equal(list1, list2)
        MemoryGame.play(diff)
    elif game_num == "2":
        print(f"You chose the Guess Game with difficulty of {diff}, good luck!")
        y = GuessGame.guess_class()
        y.guess()
    elif game_num == "3":
        print(f"You chose the Currency Roulette with difficulty of {diff}, good luck!")
        z = CurrencyRouletteGame.CurrencyGuessingGame_class
        z.play()
        # def get_x(game_diff):
        #     return game_diff
load_game(game_num, game_diff)
