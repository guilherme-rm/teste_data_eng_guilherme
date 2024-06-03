## Pipeline de ETL simplificada

A fim de se executar o programa, inicialmente é necessário instalar os requisitos:

`pip install -r requirements.txt`

Os scripts que criam os bancos de dados estão dentro da pasta `setup`. Eles podem ser executados por meio do comando `./setup.sh`

No arquivo `setup/vars.py` estão definidas as variáveis de user e password para se rodar o arquivo localmente. Essas variáveis devem ser alteradas para as configurações de usuário e senha do servidor de PostgreSQL utilizado.

Caso haja erro na execução, para permitir a execução da aplicação sem alterar o arquivo `setup/vars.py`, basta executar os seguintes comandos no terminal:

`sudo -u postgres psql`

Em seguida:

`ALTER USER postgres WITH PASSWORD 'password';`

Após a execução sem erros do script `setup.sh`, os bancos de dados fonte e alvo foram criados, e a aplicação pode ser executada.

Para isso, em uma janela de terminal o comando a seguir deve ser executado: `uvicorn main:app --reload`

Em seguida, em outra janela de terminal: `python client.py`

O script `client.py` utiliza o arquivo `input.json` como entrada. Para consultas adicionais alem das exemplificadas, basta adicionar ou substituir entradas conforme o modelo:

`{
            "date" : <nova data e horário a serem consultadas>,
            "names" : [<variáveis a serem consultadas>]
        }`

A aplicação apresentará os dados desejados no terminal, além de escrever nas tabelas no banco de dados alvo conforme especificado.

## Informações sobre os bancos de dados

Período de tempo utilizado: 10 dias contados por minuto a partir de 01/01/2024 - 00:00:00.

No banco de dados alvo, a coluna id da tabela signal foi considerada como sendo o número da consulta realizada.

## A fazer

Possibilitar a execução da aplicação por meio do docker, de modo que não seja necessário alterar usuário e senha localmente.