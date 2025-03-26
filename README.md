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

## 🛠️ Project Structure

fast_api_structure/ ├── app/ # Main FastAPI app │ ├── api/ # API routes │ ├── core/ # Configuration │ ├── crud/ # Business logic │ ├── db/ # DB models & connection │ ├── schemas/ # Pydantic models │ └── main.py # App entry point ├── docker/ # MySQL config/init ├── docker-compose-mysql.yml # Docker Compose config for DB ├── Makefile # Command automation ├── requirements.txt # Main dependencies ├── requirements-dev.txt # Dev tools like black, isort, etc. └── README.md # This file


---

## 🚀 Getting Started

### 🔧 1. Clone the repo

```bash
git clone https://github.com/yourname/fast_api_structure.git
cd fast_api_structure

🐍 2. Create virtual environment

make create_env

📦 3. Install dependencies

make install_deps

🐳 4. Start MySQL using Docker

make db_up

🛠 5. Initialize the database

make init_db

🚀 6. Run the FastAPI server

make run_server




🧪 Example API Endpoints
GET / → Hello, World!

POST /api/v1/users – create a new user

GET /api/v1/users – list all users

GET /api/v1/users/{id} – get user by ID

PUT /api/v1/users/{id} – update user

DELETE /api/v1/users/{id} – delete user



🛡️ License
MIT License


MIT License

Copyright (c) 2025 Master Soy Vitou

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
