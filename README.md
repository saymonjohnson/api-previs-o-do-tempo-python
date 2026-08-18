Conversor de Moedas e Histórico Cambial (API & SQLite)

Um script em Python desenvolvido para automatizar a consulta de taxas de câmbio em tempo real, realizar conversões financeiras e persistir o histórico de consultas em um banco de dados relacional.

## Tecnologias Utilizadas
* **Python 3**
* **SQLite3:** Para armazenamento e histórico das cotações.
* **Requests:** Para consumo da API REST externa.
* **HG Brasil Finance API:** Fonte dos dados cambiais.

## Funcionalidades
1. **Consumo de API:** Realiza requisições HTTP GET para buscar o valor atualizado do Dólar (USD) e do Euro (EUR).
2. **Lógica de Conversão:** Recebe um valor em Reais (BRL) via input do usuário e calcula a conversão exata com base na cotação do momento.
3. **Persistência de Dados (CRUD):** Cria automaticamente um banco de dados `cambio.db` e insere os valores pesquisados, juntamente com um *timestamp* (data e hora exatas da consulta).
4. **Leitura de Histórico:** Consulta o banco de dados para recuperar e exibir a última transação registrada.

## Como executar

1. Clone o repositório.
2. Instale a biblioteca requests (caso não tenha):
   ```bash
   pip install requests
