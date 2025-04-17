import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

class ConnectionHandler:
    def __init__(self):

        try:
            success = load_dotenv()
            if not success:
                raise EnvironmentError("Failed to load environment variables from .env file.")
            
            self.connection = None
            self.cursor = None
            self.db_config = {
                "host": os.getenv("DB_HOST"),
                "dbname": os.getenv("DB_NAME"),
                "user": os.getenv("DB_USER"),
                "password": os.getenv("DB_PASSWORD")
            }
        except Exception as e:
            print("Error loading environment variables from .env file.", e)
           
       



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

    
