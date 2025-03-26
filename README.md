# 🚀 FastAPI Pro Project

This is a professional backend project using **FastAPI**, **MySQL**, **Docker**, and **SQLAlchemy (async)**. It’s structured for scalability, developer happiness, and clean architecture.

---

## 📦 Tech Stack

- **FastAPI** – lightning-fast Python web framework  
- **SQLAlchemy (async)** – async DB access  
- **MySQL 8** – production-grade relational DB  
- **Docker** – containerized database  
- **Pydantic v2** – schema validation  
- **Uvicorn** – ASGI server  
- **Makefile** – automated CLI commands  
---


## 🚀 Getting Started

### 🔧 1. Clone the repo

```bash
git clone https://github.com/yourname/fast_api_structure.git

```

```bash
cd fast_api_structure
```

### 🐍 2. Create virtual environment

```bash
make create_env
```

### 📦 3. Install dependencies

```bash
make install_deps
```

### 🐳 4. Start MySQL using Docker

```bash
make db_up
```

### 🛠 5. Initialize the database

```bash
make init_db
```

### 🚀 6. Run the FastAPI server

```bash
make run_server
```




### 🧪 Example API Endpoints

```bash
GET / → Hello, World!

POST /api/v1/users – create a new user

GET /api/v1/users – list all users

GET /api/v1/users/{id} – get user by ID

PUT /api/v1/users/{id} – update user

DELETE /api/v1/users/{id} – delete user
```


### MIT License

Copyright (c) 2025 Master Soy Vitou

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)