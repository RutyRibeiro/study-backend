from flask import Flask, request, current_app
from flask_cors import CORS, cross_origin
import json, funcoes, cryptography



context = ('server.cert','server.key')
# context.use_privatekey_file('.\certificates\server.key')
# context.use_certificate_file('.\certificates\server.crt')


app = Flask("Teste")
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/": {"origins": "*"}})

@app.route('/cadastro', methods=['POST'])
@cross_origin(origin='*',headers=['Content- Type'])
def cadastro():
    body={}
    body['nome']= request.form['nome']
    video= request.files['video']
    body['video'] = funcoes.downloadVideo(video)
    print (body)
    # body=json.loads(request.data,strict=False)
    resp=funcoes.cadastro(body)
    return resp

@app.route('/', methods=['GET'])
def get():
    return {'ok': 'ok'}

app.run(ssl_context=context)