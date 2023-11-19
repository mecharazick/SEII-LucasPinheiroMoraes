from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        variavel = "Game: Adivinhe o número correto"
        return render_template('index.html', variavel=variavel)
    elif request.method == 'POST':
        numero = 0
        palpite = int(request.form.get('name'))
        if numero == palpite:
            return '<h1>Você ganhou!</h1>'
        else:
            return '<h1>Você perdeu!</h1>'
    else:
        return error('Metodo inválido')


@app.route('/<string:nome>')
def error(nome):
    variavel = f'Página {nome} não encontrada'
    return render_template('error.html', variavel=variavel)
