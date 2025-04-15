import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

class ConnectionHandler:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.db_config = {
            os.getenv("DB_HOST"): os.getenv("DB_HOST"),
            os.getenv("DB_NAME"): os.getenv("DB_NAME"),
            os.getenv("DB_USER"): os.getenv("DB_USER"),
            os.getenv("DB_PASSWORD"): os.getenv("DB_PASSWORD")
        }

    def connect(self):
        try:
            self.connection = psycopg2.connect(**self.db_config)
            self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
            print("Database connection established.")
        except Exception as e:
            print(f"Error connecting to database: {e}")
            raise

    def execute_query(self, query, params=None):
        try:
            if self.cursor:
                self.cursor.execute(query, params)

                if query.strip().lower().startswith("select"):
                    return self.cursor.fetchall()
                self.connection.commit()
                print("Query executed successfully.")

            else:
                print("Cursor is not initialized.")
        except Exception as e:
            print(f"Error executing query: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    
