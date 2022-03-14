from flask import Flask,jsonify
from flask_restful import Api
from resources.medicamentos import Medicamentos
from resources.inicio import Main

app = Flask(__name__)

api = Api(app)

api.add_resource(Medicamentos, '/medicamentos')
api.add_resource(Main, '/')


if __name__ == '__main__':
    app.run(debug=True)