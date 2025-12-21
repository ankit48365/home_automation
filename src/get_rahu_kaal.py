import requests

API_URL = "https://json.freeastrologyapi.com/rahu-kalam"
API_KEY = "VT0mrAZWf64oIqoTgUfZg6AmH91Cfasv87YYOxbR"

payload = {
    "year": 2029,
    "month": 2,
    "date": 10,
    "hours": 12,
    "minutes": 1,
    "seconds": 0,
    "latitude": 43.2081,    # Concord, NH
    "longitude": -71.5376,  # Concord, NH
    # "latitude": 42.3603,   # Boston
    # "longitude": -71.0583, # Boston
    "timezone": -5         # EST (UTC-5)
}

headers = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY
}

def get_rahu_kalam():
    response = requests.post(API_URL, json=payload, headers=headers)
    print("Status code:", response.status_code)
    try:
        data = response.json()
        print("Response JSON:")
        print(data)
    except Exception:
        print("Raw response text:")
        print(response.text)

if __name__ == "__main__":
    get_rahu_kalam()
