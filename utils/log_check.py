from datetime import datetime,timedelta
import logging
import os

logging.basicConfig(filename='logs.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
data_limite = datetime.now() - timedelta(days=2)



def LogCheck():
    for arquivo in os.listdir(os.path.dirname(__file__)):
     if arquivo.endswith('.log'):
          data = open(arquivo)
          data_arquivo_str = data.read(19)
          data.close
          data_arquivo = datetime.strptime(data_arquivo_str, '%Y-%m-%d %H:%M:%S') 
          if data_arquivo < data_limite:            
                data= open(arquivo,'w')
                data.close()