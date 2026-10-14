from flask import Flask
from random import randint

app = Flask(__name__)

number_to_guess = randint(0, 9)

@app.route("/<int:number>")
def hello_world(number):
    if number_to_guess == number:
        return "<h3 style='color: red;'>Correct guess!Congratulations!</h3>" \
        "<img src='https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bjN0cTg2aWZ4amlsMXBiOTFkeWluZ3YwNzNram1oNmc5M2Q3bzl1byZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/Zwkxqa2c6C4avWnrq3/giphy.gif' alt='Correct guess!'>"
    elif number_to_guess > number:
        return "<h3 style='color: blue;'>Too low! Try again!</h3>"\
        "<img src='https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3bjN0cTg2aWZ4amlsMXBiOTFkeWluZ3YwNzNram1oNmc5M2Q3bzl1byZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/D94a6xlwwsujwzUQGd/giphy.gif' alt='Too low!'>"
    elif number_to_guess < number:
        return "<h3 style='color: green;'>Too high! Try again!</h3>" \
        "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOW8ybDhxb255OGxrM3NuZmowMTd6YnFhcjlrbDM4bDU4cnEwZ3lqeiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/UFRtykmfyBA8F7qPh9/giphy.gif' alt='Too high!'>"
    else:
        return "<p>Try again!</p>"

@app.route("/")
def home():
    return "<h1 style='text-align: center;'>Guess a number between 0 and 9</h1>"\
    "<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeW4xeXltbjE3cWpsbTl4azR1ZDg4dnA0ZGJ4dDAzMDl3MzFybDUxYSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/VplOPZ7BD85nT9lhMf/giphy.gif' style='display: block; margin-left: auto; margin-right: auto;' alt='Guess a number'>"

if __name__ == "__main__": # __main__ is a special variable in Python that represents the name of the current module. When a Python script is run directly, the value of __name__ is set to "__main__". This allows you to check if the script is being run directly or being imported as a module in another script. If it is being run directly, the code block under this condition will execute, which in this case starts the Flask application with debug mode enabled.
    app.run(debug=True)