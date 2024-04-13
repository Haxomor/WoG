import random
import time
import os

def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(int(difficulty))]

def get_list_from_user(difficulty):
    sequence = generate_sequence(difficulty)
    print("Remember the numbers: ")
    print(sequence)
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
    input_text = "Enter {} numbers separated by spaces: ".format(difficulty)
    user_input = input(input_text).strip().split()
    return [int(num) for num in user_input]

def is_list_equal(list1, list2):
    return list1 == list2

def play(difficulty):
    user_sequence = get_list_from_user(difficulty)
    return is_list_equal(generate_sequence(difficulty), user_sequence)


# Example usage:

