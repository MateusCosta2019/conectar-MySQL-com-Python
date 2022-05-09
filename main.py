import logging
from datetime import datetime
from modulo.conecta_db import conecta_db

data = datetime.today().strftime('%d_%m_%Y')

# Cria e configura arquivo de log
logging.basicConfig(filename=f'log\\log_{data}.log',
                    format='%(asctime)s %(message)s',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def conn_db():
    try:
        connection = conecta_db()
        logging.debug('Conexão realizada com sucesso')
    except Exception as err:
        logging.error('Não foi possivel realizar conexão pelo detemrinado erro:', err)

if __name__ == '__main__':
    conn_db()