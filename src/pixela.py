import requests
import datetime
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")

endpoint = "https://pixe.la/v1/users"

config = {"token": TOKEN,
          "username": USERNAME,
          "agreeTermsOfService": "yes",
          "notMinor": "yes"}

# response = requests.post(url = endpoint, json = config)
# print(response.text)


headers = {"X-USER-TOKEN": TOKEN}

GRAPH = "tomato-farm-1"

graph_config = {"id": GRAPH,
                "name": "Get A Job",
                "unit": "tomatoes",
                "type": "int",
                "color": "momiji",
                "timezone": "America/Denver",
                "startOnMonday": True,
                }

# response = requests.post(url = f"{endpoint}/{USERNAME}/graphs", json = graph_config, headers=headers)

# print(response.text)

pixel_config = {"date": datetime.datetime.now().strftime("%Y%m%d"),
                "quantity": "1",
                }

# response = requests.post(url = f"{endpoint}/{USERNAME}/graphs/{GRAPH}", json=pixel_config, headers=headers)

# print(response.text)

response = requests.get(url = f"{endpoint}/{USERNAME}/graphs/{GRAPH}")

with open("graph.svg", "w", encoding="utf-8") as f:
    f.write(response.text)