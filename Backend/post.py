
from flask import Flask, request
import funcoes

app = Flask("Teste")

@app.route('/helloworld', methods=['POST'])
def teste():
    body = request.get_json()
    teste = funcoes.cadastro(body)
    return (teste)


app.run()