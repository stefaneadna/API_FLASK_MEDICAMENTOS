from flask_restful import Resource,reqparse
import pandas as pd
import json
from flask import request
from sqlalchemy import null

class Medicamentos(Resource):

    def get(self):              
        data = {
        "laboratorio": request.args.get('laboratorio'),
        "produto": request.args.get('produto'),
        "registro": request.args.get('registro'),
        "substancia": request.args.get('substancia'),
        "tarja": request.args.get('tarja')
        }

        lista_cond = []
        lista_cond.append("PRODUTO")
        df = pd.read_csv('TA_PRECO_MEDICAMENTO.csv', encoding="Windows-1252", sep = ';')

        if data["laboratorio"] is not None:
            lista_cond.append("LABORATÓRIO")
            data_request = data['laboratorio']
            if(data_request!=''):
                df = df.query("LABORATÓRIO==@data_request")
            print(data_request)
        
        if data["produto"] is not None:
            data_request = data["produto"]
            if(data_request!=''):
                df = df.query("PRODUTO==@data_request")
            print(data_request)
        
        if data["registro"] is not None:
            lista_cond.append("REGISTRO")
            data_request = data["registro"]
            if(data_request!=''):
                df = df.query("REGISTRO==@data_request")
            print(data_request)
                
        if data["substancia"] is not None:
            lista_cond.append("SUBSTÂNCIA")
            data_request = data["substancia"]
            if(data_request!=''):
                df = df.query("SUBSTÂNCIA==@data_request")
            print(data_request)

        if data["tarja"] is not None:
            lista_cond.append("TARJA")
            data_request = data["tarja"]
            if(data_request!=''):
                df = df.query("TARJA==@data_request")
            print(data_request)

        df_1 = df[lista_cond]
        result = df_1.to_json(orient="records")
        parsed = json.loads(result)
        return parsed
        



##http://127.0.0.1:5000/medicamentos?substancia=subs1&laboratorio=lab1&produto=prod1&tarja=tarja1&registro=reg1

# result = df[lista_cond].to_json(orient="records")
#             parsed = json.loads(result)
#             return parsed