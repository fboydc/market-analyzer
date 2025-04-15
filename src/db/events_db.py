from db.db_connection_handler import ConnectionHandler
from ..data_fetcher.models.event import Event

class event_model:
    def _init_(self):
        self.dbConnection = ConnectionHandler()
    
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
        
    def insert_event(self, event_data: Event): 
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

    def delete_event(self, event_id):
        query = "DELETE FROM events WHERE id = %s"
        try:
            self.dbConnection.execute_query(query, (event_id,))
        except Exception as e:
            print(f"Error deleting event: {e}")