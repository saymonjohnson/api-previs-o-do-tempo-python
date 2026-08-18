# Consulta de Previsão do Tempo (API REST)

Script em Python voltado para o consumo de APIs externas, tratamento de respostas em formato JSON e exibição de dados meteorológicos dinâmicos no terminal.

## Tecnologias Utilizadas
* **Python 3**
* **Requests:** Biblioteca para requisições HTTP.
* **HG Brasil Weather API:** Fornecimento dos dados meteorológicos.

## Funcionalidades
O sistema permite que o usuário digite a sigla de uma Unidade Federativa (UF) e retorna instantaneamente:
* Temperatura e Condição do tempo atual.
* Porcentagem de umidade e velocidade do vento.
* Horário exato do nascer e do pôr do sol.
* Identificação de turno (dia/noite) diretamente pelo payload da API.

## Como executar

1. Clone o repositório.
2. É necessário possuir uma chave válida da HG Brasil. Substitua a string `seu_api_key` no código pela sua chave.
3. Instale a biblioteca requests:
   ```bash
   pip install requests
