set shell := ["cmd.exe", "/c"]

venv:
    python -m venv .venv

install: venv
    .venv\Scripts\activate.bat && pip install -r requirements.txt

serve: install
    .venv\Scripts\python.exe -m uvicorn backend:app


get_test_database: install
    .venv\Scripts\python.exe init_db.py

clear_database: install
    .venv\Scripts\python.exe clear_db.py

up: install get_test_database serve


