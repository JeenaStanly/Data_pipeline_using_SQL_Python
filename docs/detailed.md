# Using psycopg2 with PostgreSQL in Python

This guide explains how to use the `psycopg2` library to connect to a PostgreSQL database in a Python project.

---

## 📦 What is psycopg2?

`psycopg2` is a PostgreSQL adapter for Python. It allows Python code to interact with a PostgreSQL database using standard SQL commands.

---

## 🔧 Installing psycopg2

You can install it using `pip`. There are two options:

### Standard version:
```bash
pip install psycopg2
 
```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="your_database",
    user="your_user",
    password="your_password"
)

cursor = conn.cursor()
print("Connection successful!")


from sqlalchemy import create_engine

# Create a PostgreSQL connection using psycopg2
engine = create_engine("postgresql+psycopg2://user:password@localhost:5432/dbname")
