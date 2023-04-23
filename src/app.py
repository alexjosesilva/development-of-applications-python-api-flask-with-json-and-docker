from flask import Flask, jsonify, request, json
from flask_restful import Api
from json import dumps

app = Flask(__name__)
api = Api(app)

#dados iniciais
dados = [
            {
                "id":1,
                "name_city": "Dublin",
                "country": "Ireland"
            }
    ]

# Listar todos registros
@app.route("/listar",  methods = ['GET'])
def listarTodos():
     return jsonify(dados)

# salvar um registro
@app.route("/salvar",  methods = ['POST'])
def salvar():  
    dados.append(request.get_json())
    return jsonify(dados)

#atualizar um registro
@app.route("/atualizarItem/<id>",  methods = ['PUT'])
def atualizar(id):
     
    for key in dados:
       if(dumps(key['id']) == id):
            dados[dados.index(key)] = request.get_json()
            return dados
                   
    return []
    
    
#deletar um registro
@app.route("/deletar/<id>",  methods = ['DELETE'])
def deletar(id):
    for key in dados:
        if(dumps(key['id']) == id):
            dados.remove(key)
            return dados
                   
    return []

#procurar um registro
@app.route("/procurar/<name_city>",  methods = ['GET'])
def procurar(name_city):
    for key in dados:
        if key['name_city'] == name_city:
            return jsonify(dados[dados.index(key)])
                   
    return []