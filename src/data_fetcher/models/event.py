class Event:
    def __init__(self, event_id: str, event_name: str, event_date: str, event_time: str = None, event_country: str = None, event_importance: str = None):
        
        self.id = event_id
        self.name = event_name
        self.date = event_date
        self.country = event_country
        self.importance = event_importance
        self.time = event_time

def get_event_id(self):
        return self.id

def get_event_name(self):
        return self.name

def get_event_date(self):
        return self.date

def get_event_country(self):
        return self.country

def get_event_importance(self):
        return self.importance

def get_event_time(self):
        return self.time



        self.id = event_id

def set_event_name(self, event_name: str):
        self.name = event_name

def set_event_date(self, event_date: str):
        self.date = event_date

def set_event_country(self, event_country: str):
        self.country = event_country
    
def set_event_importance(self, event_importance: str):
        self.importance = event_importance

def set_event_time(self, event_time: str): 
        self.time = event_time

def __repr__(self):
        return f"Event(event_id={self.event_id}, event_name={self.event_name}, event_date={self.event_date})"