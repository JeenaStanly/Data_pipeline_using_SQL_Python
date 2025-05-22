import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME")

# Create the database engine
engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Step 1: Extract
df = pd.read_csv("data/employees.csv")

# Step 2: Transform
# Fill missing ages with median age
df['age'].fillna(df['age'].median(), inplace=True)

# Fill missing salaries with median salary
df['salary'].fillna(df['salary'].median(), inplace=True)

# Step 3: Load
df.to_sql('employees', con=engine, if_exists='replace', index=False)

print("✅ ETL process completed and data loaded into MySQL.")
