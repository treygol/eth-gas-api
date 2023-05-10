import requests
import time

api_key = "6ZZA1NUFBBZN5DGFD8Q6M67R7H7WC92T4A"

while True:
    response = requests.get(f"https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={api_key}")
    data = response.json()["result"]
    print(f"low: {data['SafeGasPrice']}")
    print(f"average: {data['ProposeGasPrice']}")
    print(f"high: {data['FastGasPrice']}")

    time.sleep(6)