import requests

from .. import config


class APODManager:
    def __init__(self):
        self.apod_key = config.api_key
        self.apod_url = config.apod_url

    
    def get_apod(self):
        url = f"{self.apod_url}?api_key={self.apod_key}"
        response = requests.get(url)
        if response.status_code != 200:
            return {"error": "An error occurred while fetching the APOD data"}, 400
        return response.json()

async def trigger_tick(url):
    
    payload = {
            "event_name": "NASA Picture of the Day",
            "message": "Hello From NAPOD",
            "status": "success",
            "username": "NAPOD"
        }

    requests.post(
            url,
            json=payload,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        )
