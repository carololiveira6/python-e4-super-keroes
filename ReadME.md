## **Table of Contents**
- [E4 - Super Keroes CSV](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1b_e_02_super-keroes.html&ref=master#mcetoc_1etk5nns41)
  - [Objetivo](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1b_e_02_super-keroes.html&ref=master#mcetoc_1f362b6b10)
  - [Preparativos](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1b_e_02_super-keroes.html&ref=master#mcetoc_1f362b6b11)
  - [Exercício 1](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1b_e_02_super-keroes.html&ref=master#mcetoc_1emem4is73)
  - [Exercício 2](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1b_e_02_super-keroes.html&ref=master#mcetoc_1emem4is72)
  - [Exercício 3](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1b_e_02_super-keroes.html&ref=master#mcetoc_1emem4is71)
- [Entregáveis](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1b_e_02_super-keroes.html&ref=master#mcetoc_1egvoav555j)
- [Critérios de aceitação](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/1b_e_02_super-keroes.html&ref=master#mcetoc_1eh146n6m3)
# **E4 - Super Keroes CSV**
Nessa entrega, você poderá colocar em prática o que aprendeu sobre ler e escrever em arquivos csv e simular como seria uma rota de **GET** e de **POST**.
## **Objetivo**
Esta entrega foi elaborada para você poder trabalhar seu conhecimento sobre leitura e escrita em arquivos CSV.
## **Preparativos**
Crie um aquivo chamado **kharacters.py** nesse aquivo você irá colocar todas suas funções.

O cabeçalho do seu **CSV** deve seguir o seguinte padrão:

id,name,intelligence,power,strength,agility

-----
## **Exercício 1**
- **find\_all\_characters(filename)**
  - **Parâmetros:**
    - filename: nome do arquivo que será aberto.
  - **Procedimento:**
    - Buscar por **todos** os personagens no arquivo CSV filename.
  - **Retorno:**
    - Retornar os personagens encontrados em formato de lista de dicionários.
    - Retornar uma **lista vazia**, caso nenhum personagem tenha sido encontrado.

**Exemplos:**

\# Exemplo 1:

filename = "characters.csv"

found\_character = find\_all\_characters(filename)

print(found\_character)

\> [{

`    `"id": 1,

`    `"name": "Hulk",

`    `"intelligence": 9,

`    `"power": 7,

`    `"strength": 10,

`    `"agility": 8

}]

## **Exercício 2**
- **find\_character\_by\_id(filename, character\_id)**
  - **Parâmetros:** 
    - filename: nome do arquivo que será aberto.
    - character\_id: identificador único de cada personagem, representado pelo fieldname id.
  - **Procedimento:**
    - Buscar pelo personagem com **id igual** a character\_id.
  - **Retorno:**
    - Retornar o personagem encontrado no **formato de dicionário**.
    - Retornar None caso não tenha sido encontrado.

**Exemplos:**

\# Exemplo 1:

filename = "characters.csv"

character\_id = 1

found\_character = find\_character\_by\_id(filename, character\_id)

print(found\_character)

\> {

`    `"id": 1,

`    `"name": "Hulk",

`    `"intelligence": 9,

`    `"power": 7,

`    `"strength": 10,

`    `"agility": 8

}

\# Exemplo 2:

filename = "characters.csv"

character\_id = 2

found\_character = find\_character\_by\_id(filename, character\_id)

print(found\_character)

\> None

## **Exercício 3**
- **create\_character(filename, \*\*kwargs)**
  - **Parâmetros:**
    - filename: nome do arquivo a ser escrito.
    - \*\*kwargs: os dados do personagem que será criado.
- **Procedimento:**
  - Se certificar de que existe fieldnames para o arquivo filename.
  - Obter o id do novo personagem a ser criado (pegar o último id cadastrado e adicionar um).
  - Inserir um novo personagem no arquivo filename.
- **Retorno:**
  - Retornar o personagem criado em **forma de dicionário**.

**Exemplos:**

\# EXEMPLO 1:

filename = "characters.csv"

new\_character = {

`    `"name": "Hulk",

`    `"intelligence": 9,

`    `"power": 7,

`    `"strength": 10,

`    `"agility": 8

}

created\_character = create\_character(filename, \*\*new\_character)

print(created\_character)

\> {

`    `"id": 1,

`    `"name": "Hulk",

`    `"intelligence": 9,

`    `"power": 7,

`    `"strength": 10,

`    `"agility": 8

}
## -----
# **Entregáveis**
**Repositório**

- Link do **repositório** do **GitLab**
- **Código-fonte:**
  - Arquivo **kharacters.py**.
- **Privacidade**
  - Incluir **ka-br-out-2020-correcoes** como **reporter**.
-----
# **Critérios de aceitação**

|**pts**|**Dado**|**Quando**|**É esperado**|
| :-: | :-: | :-: | :-: |
|3.5|Função create\_character |Executada com seus devidos parâmetros|Um novo **personagem é criado no arquivo** com nome especificado em filename, a função **retorna o personagem criado** em forma de dicionário, **contendo o id** do personagem|
|3.5|Função find\_character\_by\_id|Executada com seus devidos parâmetros|Um **personagem é buscado** e **retornado em formato de dicionário**|
|3|Função find\_all\_characters|Executada com seus devidos parâmetros|Uma **lista de personagens em forma de dicionário** é buscada e retornada|

**Boa diversão, devs!🦸‍♂️**

