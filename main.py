import requests
import json

url = "https://deviations.integration.sl.se/v1/messages"

params = [
    ("future", "false"),
    ("line", "40"),
    ("line", "41"),
    ("transport_mode", "TRAIN")
]

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    for deviation in data:
        header = deviation['message_variants'][0]['header']
        details = deviation['message_variants'][0]['details']
        lines = [line['designation'] for line in deviation['scope']['lines']]
        valid_from = deviation['publish']['from']
        valid_to = deviation['publish']['upto']

        print("==== PENDLINGSSTÖRNING ====")
        print(f"Rubrik: {header}")
        print(f"Detaljer: {details}")
        print(f"Gäller linjer: {', '.join(lines)}")
        print(f"Gäller från: {valid_from} till: {valid_to}")
        print()
