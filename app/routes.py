from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    titulo = 'Home'
    nome = 'sou uma variavel python'
    return render_template('index.html', nome=nome, titulo = titulo)

@app.route('/contato')
def contato():
    titulo = 'Contato'
    informacoes = {'telefone': '96237831', 'email': 'email@email.com'}
    return render_template('contato.html', informacoes=informacoes, titulo = titulo)
