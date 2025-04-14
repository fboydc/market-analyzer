import requests
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from typing import Optional
import datetime
"""
Description:
This script scrapes economic events from a website and provides functionality to filter and save the events.
The date used is hardwired to the current date. In the future we might want to add the ability to scrape past events.
However this will require a different library to simulate user navigation in order to access the historical data.

Currently we only support the content at investing.com, as this has been the most reliable source for economic events.

Parameters (For future use):
- base_url: The base URL of the economic calendar page.
"""
class EconomicEventsScraper:
    def __init__(self, base_url:  Optional[str] = None, from_date: Optional[str] = None, to_date: Optional[str] = None, date: Optional[str] = None):
        self.base_url = base_url or "https://www.investing.com/economic-calendar/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

    def fetch_html(self):
        """
        Fetches the HTML content of the economic calendar page.
        Returns:
            Raw HTML string if successful, None otherwise.

        """
        options = Options()
        options.add_argument("--headless=new")  # Run in headless mode
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        try:
            driver.get(self.base_url)
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.ID, "economicCalendarData")) 
            )

            return driver.page_source
                
        except Exception as e:
            print(f"Error fetching HTML: {e}")
            return None

    def fetch_mock_html(self):
        """
        Fetches mock HTML content for testing purposes.
        Returns:
            Mock HTML string.
        """
        file_path = os.path.join(os.path.dirname(__file__), "test_data", "sample_html.txt")

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def parse_events(self, raw_data):
        """
        Parses the HTML to extract economic events.

        Args:
            html (str): Raw HTML content.

        Returns:
            List of structured event dictionaries.
        """
        soup = BeautifulSoup(raw_data, 'html.parser')
        cols = []
        events = []
        table = soup.find(id="economicCalendarData")
        rows = table.find_all("tr")
        if not rows:
                print("No rows found in the table.")
                return None
        
        for row in rows:
            cols = row.find_all("td")
            if len(cols) < 6:
                continue
            try:
                event = {
                    "event_time": cols[0].text.strip(),
                    "country": cols[1].text.strip(),
                    "ranking": self.parse_importance(cols[2]),
                    "event": cols[3].text.strip(),
                    "actual": cols[4].text.strip(),
                    "market_exp": cols[5].text.strip(),
                }
                events.append(event)
            except Exception as e:
                print(f"Error parsing row: {e}")
                continue
        return events

   
    def parse_importance(self, importance_html):
        icons = importance_html.find_all("i", class_="grayFullBullishIcon")
        importance = len(icons)
        return importance
    
    def save_events(self, events):
        # Placeholder for saving the parsed events to a database or file
        print(events)

    def run(self, debug: bool = False):
        if debug == True:
            raw_html = self.fetch_mock_html() # fetch html directly from sample file
        else:
            raw_html = self.fetch_html() # Use selenium 
        events = self.parse_events(raw_html)
        self.save_events(events)


if __name__ == "__main__":
    scraper = EconomicEventsScraper()
    scraper.run(debug=True)
