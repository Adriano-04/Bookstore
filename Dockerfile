# Imagem base com Python 3.12 slim
FROM python:3.12-slim AS python-base

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    PATH="/opt/poetry/bin:/opt/pysetup/.venv/bin:$PATH"

# Instala dependências do sistema
RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    build-essential \
    libpq-dev \
    gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala o Poetry 1.7.1
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /opt/poetry/bin/poetry /usr/local/bin/poetry

# Define o diretório de instalação dos pacotes
WORKDIR $PYSETUP_PATH

# Copia arquivos de dependência e instala
COPY poetry.lock pyproject.toml ./

# Instala dependências (inclusive os grupos, se definidos)
RUN poetry install --no-root --only main

# Define o diretório do app
WORKDIR /app

# Copia todo o código-fonte
COPY . /app/

# Expõe a porta usada pelo Django (ajuste se necessário)
EXPOSE 8000

# Comando padrão
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
