import httpx
import json

def transfer_data(date, names):
    url = "http://localhost:8000/transfer/"
    data = {
        "timestamp": date,
        "names": names
    }
    response = httpx.post(url, json=data)
    if response.status_code == 200:
        print("Data transfered")
    else:
        print("Error while transfering data")

if __name__ == "__main__":
    f = open('input.json')
    data = json.load(f)
    for query in data["queries"]:
        transfer_data(query["date"], query["names"])