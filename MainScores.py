from flask import Flask, render_template_string
import os

# Define the Flask app
app = Flask(__name__)

# Constants
SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1

# Function to read the score from the scores file
def read_score():
    try:
        with open(SCORES_FILE_NAME, "r") as file:
            score = int(file.read().strip())
            return score
    except Exception as e:
        print(f"Error reading score: {e}")
        return BAD_RETURN_CODE

# Route to serve the score
@app.route('/')
def score_server():
    score = read_score()
    if score == BAD_RETURN_CODE:
        return render_template_string("""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1><div id="score" style="color:red">Error reading score</div></h1>
            </body>
        </html>
        """)
    else:
        return render_template_string(f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>The score is <div id="score">{score}</div></h1>
            </body>
        </html>
        """)

if __name__ == '__main__':
    app.run(debug=True)
