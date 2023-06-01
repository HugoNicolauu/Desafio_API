from json import loads
from requests import get
from fastapi import HTTPException

def SearchCep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = get(url)
    if response.status_code == 200:
        data = loads(response.content)
        try: 
            data['erro'] 
            raise HTTPException(status_code=404,detail="Cep Invalido")
        except: 
            return data['logradouro'], data['bairro'], data['localidade']
    else:
        raise HTTPException(status_code=404,detail="Cep não Encontrado")
 