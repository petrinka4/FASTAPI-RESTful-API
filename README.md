# FASTAPI-RESTful-API
## **Features**
- RESTful API using FastAPI (Python)
- API that implements CRUD endpoints for working with all database tables
- DB include tables:
   - accounts
   - banks
   - cards
   - cities
   - clients
   - filials
   - social statuses
## **Main libraries used**
- [FASTAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic.dev/)
- [Sqlalchemy](https://www.sqlalchemy.org/)

## **Project structure**
```
.
│
├── app/                   
│   ├── routers/
│   │   ├── router_account.py
│   │   └── ... 
│   ├── operations/
│   │   ├── generalOp.py
│   │   ├── accountOp.py
│   │   ├── ...
│   ├── models/
│   │   ├── accountModel.py
│   │   ├── ...
│   │── database.py
|   │── main.py
│   └── schemas.py
│── README.md
└── requirements.txt

```
- **app/** - Root directory for the FastAPI application code.
  - **models/** - Defines database models for application entities.
  - **operations/** - Contains operations for working with tables.
  - **routers/** - Contains routers for working with the database.
  
  - **database.py** - Contains the configuration of asynchronous connection to the SQLite database using SQLAlchemy and aiosqlite.
  - **main.py** - Creates an instance of FastAPI and configures routes.
  - **schemas.py** - Contains Pydantic schemas for validating API input data.
- **requirements.txt** ── Lists Python dependencies required for the project.

## **Installation**
### **Create project**

- Clone repository.
- Create python venv
- Install MySQL
- pip install -r requirements.txt
- uvicorn app.main:app
- For the convenience of testing, use this [docs](http://127.0.0.1:8000/docs) 

