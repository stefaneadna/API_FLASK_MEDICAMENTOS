# API_FLASK_MEDICAMENTOS
Esta API viabiliza o acesso à Informações Públicas sobre os medicamentos autorizados pela anvisa. Os dados foram disponibilizados pelo Portal Brasileiro de Dados Abertos.

A base de dados pode ser consultada clicando [aqui](https://dados.gov.br/dataset/preco-de-medicamentos-no-brasil-consumidor/resource/14d7b17c-ebdf-4f1c-99c4-dd235bca7b45).

**URL:** 
- Produção: `https://apiflaskmedicamentos.herokuapp.com/`
- Desenvolvimento: `http://localhost:5000/`

**Método:** `GET`
**Parâmetros de Consulta** :

Todos os filtros são opcionais e podem ser combinados da forma que for mais conveniente:


| Parâmetro           | Observação                                                                     |Exemplo                |
| ----------------    | ---------------------------------------------------------------                | --------------------- |
| laboratorio         | Nome da empresa detentora do registro sanitário                                |`LABORATORIO SIMOES LTDA.`|
| produto             | Nome comercial dado ao medicamento                                             | `TALCO ALÍVIO` |
| registro            | Número de registro de produto junto à ANVISA.                                  | `57600510011`              |
| substancia          | Substância do produto                                                          | `SALICILATO DE FENILA;ÁCIDO SALICÍLICO;ÓXIDO DE ZINCO;ENXOFRE;MENTOL`|
| tarja               | Tarja do medicamento                                                           | `Tarja -(*)"` |
| apresentacao        | Como o medicamento é apresentado                                               | `TALQUEIRA C/ 100 G`|
| tipoProduto         | categorização do medicamento por tipo de produto                               | `Similar`                 |
| classeTerapeutica   | Classificação Anatômica de Produtos Farmacêuticos                              | `D10A - ANTIACNEICOS TÓPICOS`                   |
| restricaoHospitalar | Indica os medicamentos em embalagens hospitalares e deuso restrito a hospitais | `Não`                   |


**Exemplo**: 
- Url com todos os filtros: 

`https://apiflaskmedicamentos.herokuapp.com/medicamentos?laboratorio=LABORATORIO SIMOES LTDA.&produto=TALCO ALÍVIO&substancia=SALICILATO DE FENILA;ÁCIDO SALICÍLICO;ÓXIDO DE ZINCO;ENXOFRE;MENTOL&tarja=Tarja -(*)&apresentacao=TALQUEIRA C/ 100 G&tipoProduto=Similar&classeTerapeutica=D10A - ANTIACNEICOS TÓPICOS&restricaoHospitalar=Não`

- Curl: 

```curl
curl --request GET \
  --url 'http://127.0.0.1:5000/medicamentos?laboratorio=LABORATORIO SIMOES LTDA.&produto=TALCO ALÍVIO&substancia=SALICILATO DE FENILA;ÁCIDO SALICÍLICO;ÓXIDO DE ZINCO;ENXOFRE;MENTOL&tarja=Tarja -(*)&apresentacao=TALQUEIRA C/ 100 G&tipoProduto=Similar&classeTerapeutica=D10A - ANTIACNEICOS TÓPICOS&restricaoHospitalar=Não'
```

**Consulta com Sucesso**

```json
{
    "PRODUTO": "TALCO ALÍVIO",
    "LABORATÓRIO": "LABORATORIO SIMOES LTDA.",
    "SUBSTÂNCIA": "SALICILATO DE FENILA;ÁCIDO SALICÍLICO;ÓXIDO DE ZINCO;ENXOFRE;MENTOL",
    "TARJA": "Tarja -(*)",
    "APRESENTAÇÃO": "TALQUEIRA C/ 100 G",
    "TIPO DE PRODUTO (STATUS DO PRODUTO)": "Similar",
    "CLASSE TERAPÊUTICA": "D10A - ANTIACNEICOS TÓPICOS",
    "RESTRIÇÃO HOSPITALAR": "Não"
  }
```

## Ambiente de Desenvolvimento
> Todos os comandos devem ser executados no diretório raiz deste projeto
> Utilize o requirements.txt para instalar as dependências desse projeto
> A API está hospedada no Heroku 

`pip3 install -r requirements.txt` 

#### Execução do projeto
`python3 app.py`

## Desenvolvimento
[@doissegundos](https://github.com/doissegundos) - Padronização e organização da base de dados, Desenvolvimento da API e Deploy da aplicação.