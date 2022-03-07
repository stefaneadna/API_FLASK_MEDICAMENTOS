from flask import Flask,jsonify
from flask_restful import Api
from resources.medicamentos import Medicamentos
import pandas as pd

app = Flask(__name__)

api = Api(app)

api.add_resource(Medicamentos, '/medicamentos')


if __name__ == '__main__':
    app.run(debug=True)