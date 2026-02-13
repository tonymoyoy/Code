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

if __name__ == '__main__':
    app.run(debug=True)