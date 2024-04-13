import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

# Usage example:
# screen_cleaner()  # Call this function to clear the screen
