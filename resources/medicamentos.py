from flask_restful import Resource,reqparse
import pandas as pd
import json

class Medicamentos(Resource):
    def get(self):
        df = pd.read_csv('TA_PRECO_MEDICAMENTO.csv', encoding="Windows-1252", sep = ';')
        df_1 = df[['PRODUTO','LABORATÓRIO','REGISTRO','SUBSTÂNCIA','APRESENTAÇÃO','TARJA']]
        result = df_1.to_json(orient="records")
        parsed = json.loads(result)
        return parsed