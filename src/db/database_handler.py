import psycopg2
from psycopg2.extras import RealDictCursor

class DatabaseHandler:
    def __init__(self, db_config):
        self.connection = None
        self.cursor = None
        self.db_config = db_config

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

    
