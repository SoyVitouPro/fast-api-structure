.PHONY: create_env install_deps activate_env run_server init_db db_up db_down db_logs format clean

# === Python Environment ===
ENV_DIR=fast_api_env

create_env:
	python3 -m venv $(ENV_DIR)

install_deps:
	$(ENV_DIR)/bin/pip install --upgrade pip
	$(ENV_DIR)/bin/pip install -r requirements.txt


# === FastAPI Server ===
run_server:
	uvicorn app.main:app --host 0.0.0.0 --port 8005 --reload

# === Database Initialization ===
init_db:
	cd app && python3 -m db.init_db

# === Docker MySQL Services ===
db_up:
	docker compose -f docker-compose-mysql.yml up -d

db_down:
	docker compose -f docker-compose-mysql.yml down

db_logs:
	docker logs -f fastapi_mysql

# === Utilities ===
format:
	black app

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
