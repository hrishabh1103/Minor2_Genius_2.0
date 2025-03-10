from googleapiclient.discovery import build

API_KEY = "AIzaSyDbXZ7LlDkplrYzP_0eyYA-9EICSf32aX4"
CSE_ID = "64bb9f28e5e324819"

def google_search(query):
    service = build("customsearch", "v1", developerKey=API_KEY)
    result = service.cse().list(q=query, cx=CSE_ID).execute()
    return result["items"][0]["link"]

# Example Usage
print(google_search("Best Python courses"))
