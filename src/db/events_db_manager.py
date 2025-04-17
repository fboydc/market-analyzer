from .db_connection_handler import ConnectionHandler
from datetime import datetime

class event_model:
    def __init__(self):
        self.dbConnection = ConnectionHandler()

    def connect(self):
        try:
            self.dbConnection.connect()
        except Exception as e:
            print(f"Error connecting to database: {e}")
    
    def get_all_events(self):
       query = "SELECT * FROM events"
       try:
           return self.dbConnection.execute_query(query)
       except Exception as e:
            print(f"Error fetching events: {e}")
            return None
       
    def get_event_by_id(self, event_id):
        query = "SELECT * FROM events WHERE id = %s"
        try:
            return self.dbConnection.execute_query(query, (event_id,))
        except Exception as e:
            print(f"Error fetching event by ID: {e}")
            return None
        
    def insert_event(self, event_data: list): 
        query = """
            INSERT INTO events (event_id, event_name, event_date, event_time, event_currency, event_importance)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        event_data = (
            event_data.get_event_id(),
            event_data.get_event_name(),
            event_data.get_event_date(),
            event_data.get_event_time(),
            event_data.get_event_country(),
            event_data.get_event_importance()
        )
        try:
            self.dbConnection.execute_query(query, event_data)
        except Exception as e:
            print(f"Error inserting event: {e}")

    def insert_many(self, events: dict):
        query = """
            INSERT INTO events (event_name, event_date, event_time, country, ranking, actual_value, forecast_value)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        event_data = [
            (
                event['event_name'],
                event['event_date'],  # Assuming event_date is the current date for all events
                event['event_time'],
                event['event_country'],
                event['ranking'], 
                event['actual_value'],
                event['forecast_value'] 
            ) for event in events
        ]
        
        
        try:
            self.dbConnection.cursor.executemany(query, event_data)
            self.dbConnection.connection.commit()
            print("Multiple events inserted successfully.")
        except Exception as e:
            print(f"Error inserting multiple events: {e}")


    def delete_event(self, event_id):
        query = "DELETE FROM events WHERE id = %s"
        try:
            self.dbConnection.execute_query(query, (event_id,))
        except Exception as e:
            print(f"Error deleting event: {e}")