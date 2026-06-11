from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

@app.route('/avaliacoes')
def avaliacoes():
    return render_template('avaliacoes.html')

@app.route('/faleconosco')
def fale():
    return render_template('fale.html')

@app.route('/login')
def login():
    return render_template('login.html')