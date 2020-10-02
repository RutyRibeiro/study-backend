from flask import Flask, request
from flask_cors import CORS
import json, funcoes, cryptography


context = ('server.cert','server.key')
# context.use_privatekey_file('.\certificates\server.key')
# context.use_certificate_file('.\certificates\server.crt')


app = Flask("Teste")
# CORS(app)

@app.route('/cadastro', methods=['POST'])
def cadastro():
    body=json.loads(request.data,strict=False)
    resp=funcoes.cadastro(body)
    return resp

@app.route('/', methods=['GET'])
def get():
    return 'ok'

app.run(ssl_context=context)