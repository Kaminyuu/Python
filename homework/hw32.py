import requests
import csv
import json


response = requests.get("https://jsonplaceholder.typicode.com/todos")
data = json.loads(response.text)

with open("hw32.csv", "w") as f:
    writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=data[0].keys())
    writer.writeheader()
    for d in data:
        writer.writerow(d)

