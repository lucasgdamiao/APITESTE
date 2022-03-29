from flask import Flask, request, jsonify,render_template
import httpx
from datetime import datetime

server = Flask(__name__)

def consulta():
    lista = []
    i = 1

    while (i <= 5):
        params = {'id': str(i)}
        dicelemento = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
        dic = (dicelemento.json())[0]
        del dic["completed"]
        del dic["userId"]
        lista.append(dic)
        print(dicelemento.text)
        i = i + 1

    ts = datetime.timestamp(datetime.now())
    print(dicelemento.status_code)
    print(ts)

    return lista

@server.get('/registros')
def buscar_pessoas():

    """Mostra os 5 primeiros registros"""
    return jsonify(consulta())


@server.errorhandler(500)
def internal_server_error(e):

    """Erro do server"""
    return {"error":{"reason": "error description: internal server error"}}

server.run()

