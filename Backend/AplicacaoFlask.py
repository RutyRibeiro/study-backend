from flask import Flask, request, current_app
from flask_cors import CORS, cross_origin
import flask_modulos, os

context = ('./certificates/server.cert','./certificates/server.key')

app = Flask("Teste")
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/": {"origins": "*"}})

@app.route('/cadastro', methods=['POST'])
@cross_origin(origin='*',headers=['Content- Type'])
def cadastro():
    
    verificacao = flask_modulos.verifica(request)
    if 'erro' in verificacao:
        return verificacao
    else:
        video = verificacao['video']
        verificacao['video'] = flask_modulos.download(video)
        print (verificacao)
        resp=flask_modulos.cadastro(verificacao)
    
        return resp

@app.route('/login', methods=['POST'])
@cross_origin(origin='*',headers=['Content- Type'])
def login():
    try:
        os.remove('imagemUsuario.png')
    except:
        pass
    img = (request.files['imagemUsuario'])
    img = flask_modulos.download(img)
    resp= flask_modulos.login(img)

    return resp

app.run(host='0.0.0.0', port=3333, ssl_context=context)