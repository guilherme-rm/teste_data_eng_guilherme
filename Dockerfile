# Usar uma imagem base oficial do Python
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo de dependências para o contêiner
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o contêiner
COPY . .

# Copiar os scripts de configuração para o contêiner
COPY setup/ /setup

# Executar os scripts de configuração
RUN python /setup/create_fonte.py
RUN python /setup/gen_data_fonte.py
RUN python /setup/create_alvo.py

# Expor a porta que o servidor vai rodar
EXPOSE 8000

# Comando para rodar a aplicação FastAPI usando Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
