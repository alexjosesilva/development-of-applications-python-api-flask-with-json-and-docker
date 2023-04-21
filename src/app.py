from flask import Flask
app = Flask(__name__)

@app.route('/listausuario')
def get():
        return {
            'id': 123,
            'name':"teste",
            'age':40,
            'country':'Brazil'
        }