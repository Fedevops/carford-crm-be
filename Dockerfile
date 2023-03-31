# Imagem base
FROM python:3.9-slim-buster

# Define o diretório de trabalho
WORKDIR /app

# Copia o requirements.txt para o container
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia todo o projeto para o container
COPY . .

# Expõe a porta 8000
EXPOSE 8000

# Define as variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=nome_do_seu_projeto.settings

# Executa o comando de inicialização do servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
