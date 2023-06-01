from json import loads
from requests import get
from fastapi import HTTPException

def busca_cep(cep:str):
    """ Um metodo simples de busca de cep, ultilizando Json e requests e o site "viacep"

    Args:
        cep (str): 8 digitos no Formato -> 00000000 ou 00000-000

    Raises:
        HTTPException: Caso o status code da resposta da "viacep" não seja 200.
        HTTPException: Caso a resposta possua a chave "erro".

    Returns:
        json: {
                "cep": "",
                "logradouro": " ",
                "complemento": "",
                "bairro": " ",
                "localidade": "",
                "uf": "",
                "ibge": "",
                "gia": "",
                "ddd": "",
                "siafi": ""
              }
    """
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = get(url)
    if response.status_code == 200:
        data = loads(response.content)
        try: 
            data['erro'] 
            raise HTTPException(status_code=404,detail="Cep Invalido")
        except: 
            return data
    else:
        raise HTTPException(status_code=404,detail="Cep não Encontrado")
 