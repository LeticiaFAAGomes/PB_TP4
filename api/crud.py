from api.conexao_db import *
from api.modelos import *
import pandas as pd
from fastapi import FastAPI

app = FastAPI()
conn = conectar()
cursor = conn.cursor()


def lerDadosCsv(arquivo):
    '''
    Esta função lê dados de um arquivo .CSV e os retorna como lista.
    
    Args:
        arquivo(str): Refere-se ao caminho do arquivo .CSV a ser lido.
    
    Returns:
        dados(list[dict]): Retorna uma lista com os dados armazenados no arquivo .CSV.
    '''
    dados = pd.read_csv(f'api/tabelas/{arquivo}', encoding='UTF-8').to_dict(orient='records')
        
    return dados


def consultar_tabelas(comando, arquivo=None):
    '''
    Esta função consulta as tabelas do MySQL a partir de um comando.
    
    Args:
        comando(str): Refere-se ao comando SQL.
        arquivo(str/None): Refere-se ao nome do arquivo JSON caso exista.
    
    Returns:
        lista(list): Retorna o resultado do comando SQL.
    
    '''
    lista, armazenamento = [], []
    cursor.execute(comando)
    informacoes = cursor.fetchall()
    nomeColunas = [nome[0] for nome in cursor.description]
    
    try:
        for informacao in informacoes:
            dados = {coluna: resultado for coluna, resultado in zip(nomeColunas, informacao)}
            lista.append(Metadado(**dados))

            if arquivo:
                armazenamento.append(dados)
                criarEndpoint(armazenamento, arquivo)

    except Exception as ex:
        print(ex)
    
    return Metadado().formatar(lista) + '\n'
            
            
def criarEndpoint(armazenamento, arquivo):
    '''
    Esta função cria um endpoint dinamico.
    
    Args:
        armazenamento(list): lista com os dados da função `consultar_tabelas()`
        arquivo(str): Refere-se ao nome da rota.
    '''
    @app.get(f'/{arquivo}')
    async def get_consultas():
        '''
        Esta função assincrona cria um enpoint dinâmico.
        
        Returns:
            armazenamento(list): Retorna os dados da função `consultar_tabelas() para o endpoint.
        '''
        return armazenamento


def criar_tabelas(comando):
    '''
    Esta função cria tabelas no MySQL a partir de um comando.
    
    Args:
        comando(str): Refere-se à um comando SQL.
    '''
    try:
        cursor.execute(comando)
            
    except Exception as ex:
        print(ex)


def criar_insert(comando, valores):
    '''
    Esta função insere INSERTs em uma tabela no MySQL a partir de um comando.
    
    Args:
        comando(str): Refere-se à um comando SQL.
        valores(str): Refere-se aos dados à serem adicionados na tabela.
    '''
    try:
        cursor.executemany(comando, valores)
                
    except Exception as ex:
        print(ex)
    
    
if __name__ == '__main__':
    import uvicorn
    uvicorn.app(app, host='localhost', port=8000)