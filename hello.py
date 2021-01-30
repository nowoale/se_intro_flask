from flask import Flask
app = Flask(__name__)

imie = 'Ola'

@app.route('/')
def hello_world():
    return 'Hello, World ' + imie + ' !'

@app.route('/kto')
def co():
    return imie


@app.route('/wiadomosc')
def wiadomosc():
    return 'Hello, World!'
