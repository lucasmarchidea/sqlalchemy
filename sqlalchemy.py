# Importar bibliotecas
import pandas as pd

# Ler o arquivo Json
pd.set_option('display.max_columns', None)
caminho_do_arquivo = r"C:\Users\Luq\Desktop\sqlalchemy\V_OCORRENCIA_AMPLA.json"
df = pd.read_json(caminho_do_arquivo, encoding='utf-8-sig')
df.head(3)

# Selecionar colunas
colunas = ["Numero_da_Ocorrencia", "Classificacao_da_Ocorrência", "Data_da_Ocorrencia","Municipio","UF","Regiao","Nome_do_Fabricante","Modelo"]
df = df[colunas]
df.rename( columns={  'Classificacao_da_Ocorrência' : 'Classificacao_da_Ocorrencia'  } ,inplace=True )
df.head()

# Conexão com o bd utilizando o sqlalchemy
from sqlalchemy import create_engine, Integer, String, Date, VARCHAR, DATE

# Conexão com o banco de dados
dbname   = 'python'
user     = 'postgres'
password = '123456'
host     = 'localhost'
port     = '5432'

# String de conexão
conn_str = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'

# Criar uma conexão usando o SQLalchemy
engine = create_engine(conn_str)

# Nome da tabela no banco de dados
nome_tabela = 'anac_sqlalchemy' 

# Enviar DataFrame para o Banco de Dados

# Engine: Vai levar os dados para o banco usando essa conexão
# index=false: Ignorar o indice de posição dos dados da tabela
# Replace: Manter a tabela atualizada
df.to_sql(nome_tabela, engine, index=False, if_exists='replace',dtype={
            'Numero_da_Ocorrencia':Integer,
            'Classificacao_da_Ocorrencia':VARCHAR(50),
            'Data_da_Ocorrencia':DATE,
            'Municipio':VARCHAR(50),
            'UF':VARCHAR(30),
            'Regiao':VARCHAR(30),
            'Nome_do_Fabricante':VARCHAR(100),
            'Modelo':VARCHAR(30)
            })

# Fechar conexão
engine.dispose()


