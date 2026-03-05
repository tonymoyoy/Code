# Absurde Lottery Number Generator

This small Flask application exposes a handful of HTTP endpoints that generate random numbers for various lottery-like games. It was built for fun and allows you to easily fetch a “lucky” number (or set of numbers) via a web browser or programmatically as JSON.

## Available Endpoints

- **`/api/tris`** – returns a single integer between 0 and 99 999.
- **`/api/chispazo`** – returns an ordered list of 5 numbers between 1 and 28.
- **`/api/gana_gato`** – returns a list of eight integers between 1 and 5 (inclusive).
- **`/api/sorteo_mayor`** – returns a single integer between 0 and 60 000.
- **`/api/sorteo_superior`** – returns a single integer between 1 and 60 000.
- **`/api/zodiac_fortune`** – returns a randomly chosen zodiac sign and a number between 0 and 9 999.

When accessed from a browser, the endpoints render a simple HTML page (using the templates in `templates/`). Otherwise, they respond with JSON suitable for API clients.

## Running the App

Install dependencies (Flask) and start the server:

```bash
pip install flask
python hello.py
```

Navigate to `http://localhost:5000/` to see the front-end.


---

## 🎉 Good Luck!

> The numbers generated here are pure randomness — treat them as a bit of absurdist fun rather than a guarantee. Try your luck, enjoy the process, and **may fortune favour you**! 🍀

Happy coding and good luck in the lottery! 🧧

