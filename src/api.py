from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {
            'id': 123,
            'name':"teste",
            'age': 40,
            'country':'Brazil'
        }

api.add_resource(HelloWorld, '/listarusuario')


if __name__ == '__main__':
    app.run(debug=True)