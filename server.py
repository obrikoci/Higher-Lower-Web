from flask import Flask
import random

app = Flask(__name__)

generated_number = random.randint(0, 9)
print(generated_number)


def align_on_center(function):
    def wrapper_fn():
        return f"<center>{function()}</center>"
    return wrapper_fn


@app.route("/")
def home_page():
    return ('<center><h1>Guess a number between 0 and 9!</h1>'
            '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWoxaXMzdjl2NWF2N29temlraWh0dnNuaTdiYnpzNHVwMTgzbHF2bCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JdFEeta1hLNnO/giphy.gif" width=500></center>')


@app.route("/<int:user_number>")
def check_guess(user_number):
    if user_number < generated_number and 0 <= user_number <= 9:
        return ('<center><h1 style="color: blue">Too low, try again!</h1>'
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWE0aHdzdmp3MWRjdGMzOGxrcmM0OHNyNm54bDEzY3F3M2tueXZzcSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/gvTYmbKCwkaly/giphy.gif" width=500></center>')
    elif user_number > generated_number and 0 <= user_number <= 9:
        return ('<center><h1 style="color: red">Too high, try again!</h1>'
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExejVmbW9xY2YxNWlramYxd3AxeTI5d2dkem1veGt5bW1ndDg0bXdxMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o6ZtaO9BZHcOjmErm/giphy.gif" width=500></center>')
    elif user_number == generated_number:
        return ('<center><h1 style="color: green">You found me!</h1>'
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTU3dzcxdjNneTB5NmFpMjdpdDl2Z2MzYndmd3J1dG03NTN6MHpjbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/h5XOmB3AWFNn8JEC6G/giphy.gif" width=500></center>')
    elif user_number < 0 or user_number > 9:
        return ('<center><h1 style="color: black">Please enter a number between 0 and 9!</h1>'
                '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWJkd2liZXk5aXJ2cWhwbHJzZmU1NGZ3OWJnNHR0amd1NnJnbGltZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o8doVAxrMjXbIHaU0/giphy.gif" width=500></center>')




if __name__ == "__main__":
    app.run(debug=True)
