import requests, json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if  response.status_code == 200:
    data_json = response.json()
    data_restaurante = {}
    
    for item in data_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in data_restaurante:
            data_restaurante[nome_restaurante] = []
            
        data_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']  
        })
    
else:
    print(f'Error: {response.status_code}')
    
for nome_restaurante, data in data_restaurante.items():
    name_file = f'{nome_restaurante}.json'
    
    with open (name_file, 'w') as file_restaurante:
        json.dump(data, file_restaurante, indent=4)