from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def Olamundo():
    return 'Tetando a primeira rota, insira teste na url'

@app.route('/teste', methods=['GET'])
def teste():
    return 'Tetando a segunda rota'

if __name__ == "__main__":
    app.run(debug=True)


