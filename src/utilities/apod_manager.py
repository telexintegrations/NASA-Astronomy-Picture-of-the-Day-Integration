import requests

from .. import config


class APODManager:
    def __init__(self):
        self.apod_key = config.api_key
        self.apod_url = config.apod_url

    
    def get_apod(self):
        url = f"{self.apod_url}?api_key={self.apod_key}"
        response = requests.get(url)
        print(response.json())
        if response.status_code != 200:
            return {"error": "An error occurred while fetching the APOD data"}, 400
        return response.json()


def trigger_tick(url):
    
    NM = APODManager()
    res = NM.get_apod()

    print(res)

    message = response_formatter(res)
    print(message)

    payload = {
            "event_name": "NASA Picture of the Day",
            "message": message,
            "status": "success",
            "username": "NAPOD"
        }

    print("sending tick")
    print(payload)

    res = requests.post(
            url,
            json=payload,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        )
    print(res.json())
    if res.status_code != 202:
        print("error")
        return {"error": "An error occurred while sending the tick"}, 400
    return {"status": "success"}, 200


def response_formatter(res) -> str:
    response = f"""
        Title: **{res['title']}**
        Date: {res['date']}
        Image URL: {res['hdurl']}

        {res['explanation']}

    """

    return response