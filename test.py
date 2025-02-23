import requests

url = "https://ping.telex.im/v1/webhooks/01952fda-3658-7ddb-aa06-af3cb2462c3d"
payload = {
    "event_name": "string",
    "message": "python post",
    "status": "success",
    "username": "collins"
}

response = requests.post(
    url,
    json=payload,
    headers={
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
)
print(response.json())