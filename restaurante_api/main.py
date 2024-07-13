from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_word():
    '''
    Endpoint mensagem
    '''
    return{'Helo': 'Hello Word'}

@app.get('/api/restaurante/')
def get_restaurante(restaurante: str = Query(None)):
    
    '''
    Endpoint cardapios
    '''
    
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

    if  response.status_code == 200:
        data_json = response.json()
        
        if restaurante is None:
            return {'Data': data_json}
        
        data_restaurante = []
        
        for item in data_json:
            if item['Company'] == restaurante:
                data_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']  
                })
        return {'Restaurante': restaurante, 'Cardapio': data_restaurante}
    else:
        return{'Error': f'{response.status_code} -  {response.text}'}