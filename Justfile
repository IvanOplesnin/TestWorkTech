set shell := ["bash", "-e", "-u", "-x", "-o", "pipefail", "-c"]

default: help

venv:
    python -m venv .venv

install: venv
    . .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

serve: install
    . .venv/bin/activate
    uvicorn backend:app --reload --host 0.0.0.0 --port 8000


get_test_database: install
    . .venv/bin/activate
    python init_db.py

clear_database: install
    . .venv/bin/activate
    python clear_database.py

up: install get_test_database serve


test: install
    . .venv/bin/activate
    pytest --maxfail=1 --disable-warnings -q


