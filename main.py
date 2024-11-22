from flask import Flask  # Import Flask to create the web application
import random  # Import random for generating a random number

app = Flask(__name__)  # Create an instance of the Flask application

# Generate a random number between 0 and 9
winner = random.randint(0, 9)
print(winner)  # Print the winning number to the console for debugging

# Route for the homepage
@app.route("/")
def hello_world():
    # HTML content to display instructions on the homepage
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"
            "<h2>Place your guess in the URL after a '/' symbol!</h2>"
            "<p>e.g., http://127.0.0.1:5000/5 (if your guess was 5)</p>")

# Route for checking the user's guess
@app.route("/<int:num>")
def checker(num):
    # If the guess matches the winning number
    if winner == num:
        return ("<h1 style='color:green'>You found me</h1>"
                "<img src='https://media.giphy.com/media/hVb4xkJTGrtyaEBi6L/giphy.gif'>")
    # If the guess is higher than the winning number
    elif num > winner:
        return ("<h1 style='color:purple'>Too high!</h1>"
                "<img src='https://media.giphy.com/media/ky9vnG678kzD91TO3N/giphy.gif'>")
    # If the guess is lower than the winning number
    else:
        return ("<h1 style='color:red'>Too low!</h1>"
                "<img src='https://media.giphy.com/media/wQ2wDLXSOtIMUPIKxf/giphy.gif'>")

# Run the application in debug mode if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)
