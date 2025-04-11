# Usa uma imagem base oficial e enxuta do Python
FROM python:3.11-slim

# Evita criação de arquivos .pyc e mantém output sem buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho
WORKDIR /code

# Instala dependências do sistema (PostgreSQL client e compiladores)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Copia os arquivos de dependência e instala com Poetry
COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-root

# Copia o restante do código
COPY . .

# Copia e configura o entrypoint
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# Expõe a porta do Django
EXPOSE 8000

# Comando padrão de inicialização
CMD ["sh", "entrypoint.sh"]

