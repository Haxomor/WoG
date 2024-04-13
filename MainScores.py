# from flask import Flask, render_template_string
# import os
#
# # Define the Flask app
# app = Flask(__name__)
#
# # Constants
# SCORES_FILE_NAME = "Scores.txt"
# BAD_RETURN_CODE = -1
#
# # Function to read the score from the scores file
# def read_score():
#     try:
#         with open(SCORES_FILE_NAME, "r") as file:
#             score = int(file.read().strip())
#             return score
#     except Exception as e:
#         print(f"Error reading score: {e}")
#         return BAD_RETURN_CODE
#
# # Route to serve the score
# @app.route('/')
# def score_server():
#     score = read_score()
#     if score == BAD_RETURN_CODE:
#         return render_template_string("""
#         <html>
#             <head>
#                 <title>Scores Game</title>
#             </head>
#             <body>
#                 <h1><div id="score" style="color:red">Error reading score</div></h1>
#             </body>
#         </html>
#         """)
#     else:
#         return render_template_string(f"""
#         <html>
#             <head>
#                 <title>Scores Game</title>
#             </head>
#             <body>
#                 <h1>The score is <div id="score">{score}</div></h1>
#             </body>
#         </html>
#         """)
#
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, render_template_string, request
# import os
# import Score
#
# # Define the Flask app
# app = Flask(__name__)
#
# # Constants
# SCORES_FILE_NAME = "Scores.txt"
# BAD_RETURN_CODE = -1
#
# # Function to read the score from the scores file
# def read_score():
#     try:
#         with open(SCORES_FILE_NAME, "r") as file:
#             score = int(file.read().strip())
#             return score
#     except Exception as e:
#         print(f"Error reading score: {e}")
#         return BAD_RETURN_CODE
#
# # Route to serve the score
# @app.route('/')
# def score_server():
#     score = read_score()
#     if score == BAD_RETURN_CODE:
#         return render_template_string("""
#         <html>
#             <head>
#                 <title>Scores Game</title>
#             </head>
#             <body>
#                 <h1><div id="score" style="color:red">Error reading score</div></h1>
#             </body>
#         </html>
#         """)
#     else:
#         return render_template_string(f"""
#         <html>
#             <head>
#                 <title>Scores Game</title>
#             </head>
#             <body>
#                 <h1>The score is <div id="score">{score}</div></h1>
#             </body>
#         </html>
#         """)
#
# # Route to update the score
# @app.route('/update_score', methods=['POST'])
# def update_score():
#     name = request.form.get('name')
#     difficulty = int(request.form.get('difficulty'))
#     won = request.form.get('won') == 'True'
#
#     Score.add_score(name, difficulty, won)
#     return "Score updated successfully."
#
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template_string, request, redirect, url_for
import os
import Score

# Define the Flask app



# app = Flask(__name__)
#
# # Constants
# SCORES_FILE_NAME = "Scores.txt"
# BAD_RETURN_CODE = -1
#
# # Function to read the score from the scores file
# def read_score():
#     try:
#         with open(SCORES_FILE_NAME, "r") as file:
#             score = int(file.read().strip())
#             return score
#     except Exception as e:
#         print(f"Error reading score: {e}")
#         return BAD_RETURN_CODE
#
# # Route to serve the score
# @app.route('/')
# def score_server():
#     score = read_score()
#     if score == BAD_RETURN_CODE:
#         return render_template_string("""
#         <html>
#             <head>
#                 <title>Scores Game</title>
#             </head>
#             <body>
#                 <h1><div id="score" style="color:red">Error reading score</div></h1>
#             </body>
#         </html>
#         """)
#     else:
#         return render_template_string(f"""
#         <html>
#             <head>
#                 <title>Scores Game</title>
#             </head>
#             <body>
#                 <h1>The score is <div id="score">{score}</div></h1>
#             </body>
#         </html>
#         """)
#
# # Route to update the score
# @app.route('/update_score', methods=['POST'])
# def update_score():
#     name = request.form.get('name')
#     difficulty = int(request.form.get('difficulty'))
#     won = request.form.get('won') == 'True'
#
#     Score.add_score(name, difficulty, won)
#     return "Score updated successfully."
#
# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route('/worldOfGame', methods=['GET'])
# def score_server():
#     try:
#         with open("Scores.txt", 'r') as my_file:
#             score = my_file.read()
#         return render_template('success.html', SCORE=score)
#     except FileNotFoundError as ve:
#         return render_template('error.html', ERROR=ve)
#
# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=5001, debug=True)

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        with open('scores.txt', 'r') as file:
            score = file.read()
        html = f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1>The score is <div id="score">{score}</div></h1>
            </body>
        </html>
        """
        return html
    except Exception as e:
        error = str(e)
        html = f"""
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1><div id="score" style="color:red">{error}</div></h1>
            </body>
        </html>
        """
        return html

if __name__ == '__main__':
    app.run(debug=True)
