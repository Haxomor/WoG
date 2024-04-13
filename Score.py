
def add_score(name, difficulty, won, score_file='Scores.txt'):
    POINTS_OF_WINNING = (difficulty * 3) + 5

    if not won:
        return  # Don't update the score if the user lost

    try:
        with open(score_file, 'r') as file:
            current_data = file.readlines()
            current_scores = [line.strip().split(',') for line in current_data]
    except FileNotFoundError:
        current_scores = []

    updated_scores = []
    found = False
    for score in current_scores:
        if score[0] == name:
            found = True
            new_score = int(score[1]) + POINTS_OF_WINNING
            updated_scores.append(f"{name},{new_score}\n")
        else:
            updated_scores.append(','.join(score) + '\n')

    if not found:
        updated_scores.append(f"{name},{POINTS_OF_WINNING}\n")

    with open(score_file, 'w') as file:
        file.writelines(updated_scores)
