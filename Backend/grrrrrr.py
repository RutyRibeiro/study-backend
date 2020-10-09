from flask import Flask, request, current_app
from flask_cors import CORS, cross_origin
import json, funcoes, cryptography, os

context = ('server.cert','server.key')

app = Flask("Teste")
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/": {"origins": "*"}})

@app.route('/cadastro', methods=['POST'])
@cross_origin(origin='*',headers=['Content- Type'])
def cadastro():
    body={}
    body['nome']= request.form['nome']
    video= request.files['video']
    body['video'] = funcoes.download(video)
    print (body)
    # body=json.loads(request.data,strict=False)
    resp=funcoes.cadastro(body)
    return resp

@app.route('/login', methods=['POST'])
@cross_origin(origin='*',headers=['Content- Type'])
def login():
    try:
        os.remove('imagemUsuario.png')
    except:
        pass
    img = (request.files['imagemUsuario'])
    img = funcoes.download(img)

    resp= funcoes.login(img)

    return resp

app.run(ssl_context=context)