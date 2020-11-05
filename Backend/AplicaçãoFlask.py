from flask import Flask, request, current_app
from flask_cors import CORS, cross_origin
import funcoes, os

context = ('./certificates/server.cert','./certificates/server.key')

app = Flask("Teste")
app.config['DEBUG'] = True
app.config['TESTING'] = True
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

app.run(host='0.0.0.0', port=3333, ssl_context=context)