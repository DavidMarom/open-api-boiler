# import json
# import os
# from supabase import create_client, Client
# from dotenv import load_dotenv

# load_dotenv()
# url: str = os.getenv("SUPABASE_URL")
# key: str = os.getenv("SUPABASE_KEY")

# supabase: Client = create_client(url, key)

import psycopg2
DATABASE_URL = "postgres://david:J36aC0ld23TuAhXiWqxLcjDetxAIYmJS@dpg-cmpsek6ct0pc73f4p8dg-a.frankfurt-postgres.render.com/db01_lvmy"

def say_hello():
    return "This is the API for the api boiler app"


def create_table_users():
    # Connect to the database
    conn = psycopg2.connect(DATABASE_URL)
    # Create a cursor
    cursor = conn.cursor()
    # Execute a query
    cursor.execute("""
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    # Commit the changes
    conn.commit()
    # Close the connection
    conn.close()
    return "Table users created successfully"

def add_user():
    # Connect to the database
    conn = psycopg2.connect(DATABASE_URL)
    # Create a cursor
    cursor = conn.cursor()
    # Execute a query
    cursor.execute("""
        INSERT INTO users (name, age) VALUES ('David', 29);
    """)
    # Commit the changes
    conn.commit()
    # Close the connection
    conn.close()
    return "User added successfully"


def get_users():
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM users;
    """)
    users = cursor.fetchall()
    conn.close()
    return users