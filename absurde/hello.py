from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tris')
def tris():
    data = {'number': random.randint(0, 99999)}

    # If the client (browser) prefers HTML over JSON, render a friendly page.
    # Otherwise return machine-friendly JSON.
    accepts = request.accept_mimetypes
    if accepts['text/html'] > accepts['application/json']:
        return render_template('result.html', endpoint='/api/tris', data=data)

    return jsonify(data)

@app.route('/api/chispazo')
def chispazo():
    data = {'numbers': sorted([random.randint(1, 28) for _ in range(5)])}

    accepts = request.accept_mimetypes
    if accepts['text/html'] > accepts['application/json']:
        return render_template('result.html', endpoint='/api/chispazo', data=data)

    return jsonify(data)


@app.route('/api/gana_gato')
def gana_gato():
    # Generate 8 random integers between 1 and 5 (inclusive)
    data = {'numbers': [random.randint(1, 5) for _ in range(8)]}

    accepts = request.accept_mimetypes
    if accepts['text/html'] > accepts['application/json']:
        return render_template('result.html', endpoint='/api/gana_gato', data=data)

    return jsonify(data)

@app.route('/api/sorteo_mayor')
def Sorteo_Mayor():
    # Generate a random number between 0 and 60000 (inclusive)
    data = {'number': random.randint(0, 60000)}

    accepts = request.accept_mimetypes
    if accepts['text/html'] > accepts['application/json']:
        return render_template('result.html', endpoint='/api/sorteo_mayor', data=data)

    return jsonify(data)

@app.route('/api/sorteo_superior')
def Sorteo_Superior():
    # Generate a random number between 1 and 60000 (inclusive)
    data = {'number': random.randint(1, 60000)}

    accepts = request.accept_mimetypes
    if accepts['text/html'] > accepts['application/json']:
        return render_template('result.html', endpoint='/api/sorteo_superior', data=data)

    return jsonify(data)

@app.route('/api/zodiac_fortune')
def Zodiac_Fortune():
    # List of zodiac signs
    zodiac_signs = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 
                    'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
    
    # Pick a random zodiac sign and a random number between 0 and 9999
    data = {
        'zodiac_sign': random.choice(zodiac_signs),
        'fortune_number': random.randint(0, 9999)
    }

    accepts = request.accept_mimetypes
    if accepts['text/html'] > accepts['application/json']:
        return render_template('result.html', endpoint='/api/zodiac_fortune', data=data)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)