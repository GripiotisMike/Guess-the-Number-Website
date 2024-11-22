# Guess-the-Number-Website
This is a simple Flask-based web application where users can guess a random number between 0 and 9. The app provides visual feedback on whether the guess is too high, too low, or correct.

---

## Features
- Random number generation between 0 and 9.
- Interactive web interface with GIFs for feedback.
- Hints displayed based on the user's guess.

---

## How to Use
1. Clone the repository
2. Navigate to the project directory
3. Install the required dependencies: pip install flask
4. Run the Flask application: python main.py
5. Open your browser and navigate to: http://127.0.0.1:5000
6. Follow the instructions on the homepage to guess the number by adding your guess to the URL (e.g., http://127.0.0.1:5000/5).

---

## How It Works
- The server generates a random number between 0 and 9 when the application starts.
- Users guess the number by appending their guess to the URL.
- The server compares the guess to the winning number and responds with feedback (too high, too low, or correct) along with an appropriate GIF.
