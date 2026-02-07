from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()
database_url = os.getenv("DATABASE_URL")
engine=create_engine(database_url)
print("database_url:", database_url)
try:
    with engine.connect() as connection:
        print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")