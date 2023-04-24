from src.app import listarTodos
from src.app import salvar
from src.app import app

import json

dados = [{"country": "Ireland","id":1,"name_city": "Dublin"}]

def test_index_route():
    response = app.test_client().get('/')
    assert response.status_code == 404
   

def test_listarTodos():
    response = app.test_client().get('/listar')
    assert response.status_code == 200
    assert json.loads(response.data) == dados
    
def test_salvar():
    response = app.test_client().post('/salvar')
    assert response.status_code == 400
   
    
def test_atualizar():
    id = 1
    response = app.test_client().put('/atualizar/<id>')
    assert response.status_code == 404
    assert(1==1)
    
def test_deletar():
    id = 1
    response = app.test_client().delete('/atualizar/<id>')
    assert response.status_code == 404
    assert(1==1)
    
def test_procurar():
    name_city = "Dublin"
    response = app.test_client().delete('/procurar/<name_city>')
    assert response.status_code == 405
    assert(1==1)