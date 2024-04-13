class ScoreManager:
    POINTS_OF_WINNING = lambda difficulty: (difficulty * 3) + 5

    @staticmethod
    def add_score(difficulty):
        try:
            with open(SCORES_FILE_NAME, 'r') as file:
                current_score = int(file.read().strip())
        except FileNotFoundError:
            current_score = 0

        current_score += ScoreManager.POINTS_OF_WINNING(difficulty)

        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(current_score))
