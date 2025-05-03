# Projeto ANAC — Integração com Banco de Dados PostgreSQL

Este projeto tem como objetivo importar e transformar dados de um arquivo JSON fornecido pela ANAC (Agência Nacional de Aviação Civil), e inserir esses dados em uma tabela de um banco de dados PostgreSQL, utilizando a biblioteca SQLAlchemy em Python.

## 🔧 O que o projeto faz

- Lê dados de um arquivo JSON da ANAC.
- Seleciona e renomeia as colunas relevantes.
- Conecta-se a um banco de dados PostgreSQL utilizando SQLAlchemy.
- Cria e envia os dados para uma nova tabela no banco.
- Substitui a tabela existente sempre que o código for executado (`if_exists='replace'`).

## 📁 Fonte dos Dados

- Arquivo: `V_OCORRENCIA_AMPLA.json`
- Dados reais de ocorrências aeronáuticas disponibilizados pela ANAC.

## 🧰 Tecnologias Utilizadas

- **Python**
- **Pandas**
- **SQLAlchemy**
- **PostgreSQL**

## 🗃️ Estrutura da Tabela no Banco

| Coluna                    | Tipo          |
|---------------------------|---------------|
| Numero_da_Ocorrencia      | Integer       |
| Classificacao_da_Ocorrencia | VARCHAR(50) |
| Data_da_Ocorrencia        | DATE          |
| Municipio                 | VARCHAR(50)   |
| UF                        | VARCHAR(30)   |
| Regiao                    | VARCHAR(30)   |
| Nome_do_Fabricante        | VARCHAR(100)  |
| Modelo                    | VARCHAR(30)   |
