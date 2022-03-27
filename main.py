from flask import Flask, request, jsonify
from flask_pydantic_spec import FlaskPydanticSpec, Response, Request
from pydantic import BaseModel, Field
from tinydb import TinyDB, Query
from typing import Optional
from itertools import count


server = Flask(__name__)
spec = FlaskPydanticSpec('flask', title='Teste API')
spec.register(server)
database = TinyDB('database.json')
c =count()


class Registro(BaseModel):
    id:int
    title: str

class Lista(BaseModel):
    pessoas: list[Registro]
    count: int

@server.get('/registros/<int:id>')
@spec.validate (resp=Response(HTTP_200=Lista))
def buscar_pessoas(id):

    """Mostra todos os os registros até o ID informado"""
    try:
        return jsonify(Lista(pessoas=database.search(Query().id <=id), count=id)   .dict())
    except IndexError:
        return {'error':{"reason":"error description"}}


@server.post('/registro')
@spec.validate(body=Request(Registro), resp=Response(HTTP_201=Registro))
def inserir_pessoa():

    """Insere um registro no banco de dados"""
    VarA = request.context.body.dict()
    database.insert(VarA)
    return VarA

server.run()

