from flask_restful import Resource,reqparse
import pandas as pd
import json
from flask import request

class Medicamentos(Resource):


    def get(self):              
        data = {
        "laboratorio": request.args.get('laboratorio'),
        "produto": request.args.get('produto'),
        "registro": request.args.get('registro'),
        "substancia": request.args.get('substancia'),
        "tarja": request.args.get('tarja')
        }

        df = pd.read_csv('TA_PRECO_MEDICAMENTO.csv', encoding="Windows-1252", sep = ';')
        df_1 = df[['PRODUTO','LABORATÓRIO','REGISTRO','SUBSTÂNCIA','APRESENTAÇÃO','TARJA']]
        result = df_1.to_json(orient="records")
        parsed = json.loads(result)
        return data
        