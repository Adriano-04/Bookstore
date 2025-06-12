FROM python:3.12-slim AS python-base

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

# Instala o Poetry no diretório especificado
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=$POETRY_HOME python3 - \
    && ln -s $POETRY_HOME/bin/poetry /usr/local/bin/poetry

# Instala o psycopg2 (PostgreSQL)
RUN pip install psycopg2

# Define diretório de trabalho para dependências
WORKDIR $PYSETUP_PATH

# Copia arquivos de dependências
COPY poetry.lock pyproject.toml ./

# Instala as dependências principais
RUN poetry install --no-root --only main

# Define o diretório da aplicação
WORKDIR /app

# Copia o restante do projeto
COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
