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
        "tarja": request.args.get('tarja'),
        "apresentacao": request.args.get('apresentacao'),
        "tipoProduto": request.args.get('tipoProduto'),
        "classeTerapeutica": request.args.get('classeTerapeutica'),
        "restricaoHospitalar": request.args.get('restricaoHospitalar')
        }

        lista_cond = []
        lista_cond.append("PRODUTO")
        df = pd.read_csv('TA_PRECO_MEDICAMENTO.csv', encoding="Windows-1252", sep = ';')

        try:

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
            
            if data["tarja"] is not None:
                lista_cond.append("TARJA")
                data_request = data["tarja"]
                if(data_request!=''):
                    df = df.query("TARJA==@data_request")
                print(data_request)

            if data["apresentacao"] is not None:
                lista_cond.append("APRESENTAÇÃO")
                data_request = data["apresentacao"]
                if(data_request!=''):
                    df = df.query("APRESENTAÇÃO==@data_request")
                print(data_request)
            
            if data["tipoProduto"] is not None:
                lista_cond.append("TIPO DE PRODUTO (STATUS DO PRODUTO)")
                data_request = data["tipoProduto"]
                if(data_request!=''):
                    df = df.query("`TIPO DE PRODUTO (STATUS DO PRODUTO)`==@data_request")
                print(data_request)
            
            if data["classeTerapeutica"] is not None:
                lista_cond.append("CLASSE TERAPÊUTICA")
                data_request = data["classeTerapeutica"]
                if(data_request!=''):
                    df = df.query("`CLASSE TERAPÊUTICA`==@data_request")
                print(data_request)

            if data["restricaoHospitalar"] is not None:
                lista_cond.append("RESTRIÇÃO HOSPITALAR")
                data_request = data["restricaoHospitalar"]
                if(data_request!=''):
                    df = df.query("`RESTRIÇÃO HOSPITALAR`==@data_request")
                print(data_request)

            
            if len(lista_cond)==1:
                lista_cond.extend(["LABORATÓRIO","REGISTRO","SUBSTÂNCIA","TARJA","APRESENTAÇÃO","TIPO DE PRODUTO (STATUS DO PRODUTO)","CLASSE TERAPÊUTICA","RESTRIÇÃO HOSPITALAR"])

            df = df[lista_cond]
            result = df.to_json(orient="records")
            parsed = json.loads(result)
            return parsed,200
        except:
             return {'Message':'Ocorreu um erro, realize a requisição novamente'},400
        

