from flask_restful import Resource
class Main(Resource):
    def get(self):
        response_data = {
        "title": "Seja bem vindo a API de medicamentos cadastrados na ANVISA!!",
        "repositorio": "https://github.com/doissegundos/API_FLASK_MEDICAMENTOS",
        "Dataset": "https://dados.gov.br/dataset/preco-de-medicamentos-no-brasil-consumidor",
        "Developer": "Stefane Adna dos Santos"
        }
        return response_data;