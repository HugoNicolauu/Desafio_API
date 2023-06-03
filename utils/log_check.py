from datetime import datetime,timedelta
import logging

logging.basicConfig(filename="./Desafio_API/utils\logs.log", level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

data_limite = datetime.now() - timedelta(days=2)

def LogCheck(data_li):
    arquivo = "./Desafio_API/utils\logs.log"
    if arquivo.endswith('.log'):
        data = open(arquivo)
        data_arquivo_str = data.read(19)
        data.close
        data_arquivo = datetime.strptime(data_arquivo_str, '%Y-%m-%d %H:%M:%S') 
        if data_arquivo < data_li:            
            data= open(arquivo,'w')
            data.close()
    