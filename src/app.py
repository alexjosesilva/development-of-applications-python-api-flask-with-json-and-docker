from flask import Flask, jsonify, json, request
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

dados = [
        {
            "id":1,
            "name_city": "Dublin",
            "country": "Ireland"
        },
        {
            "id":2,
            "name_city": "Toronto",
            "country": "Canada"
        }
    ]

@app.route("/listarTodos",  methods = ['GET'])
def listarTodos():
     return jsonify(dados)
 
@app.route("/salvar",  methods = ['POST'])
def salvar():  
    dados.append(request.get_json())
    return jsonify(dados)

@app.route("/atualizarItem",  methods = ['PUT'])
def atualizar():
     return jsonify(dados)

@app.route("/deletar",  methods = ['DELETE'])
def deletar():
     return jsonify(dados)
 