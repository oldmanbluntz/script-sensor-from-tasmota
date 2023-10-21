import requests
import json

# Define the URL of your Tasmota device
url = "http://<ESP32_IP>/cm?cmnd=Status%200"

try:
    # Send an HTTP GET request to the Tasmota device
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON data from the response
        data = json.loads(response.text)

        # Extract the "AMBTMP" value directly from the JSON structure
        amb_temperature = data.get("StatusSNS", {}).get("MLX90614", {}).get("AMBTMP", None)

        if amb_temperature is not None:
            print(amb_temperature)
        else:
            print("AMBTMP not found in JSON data")
    else:
        print("HTTP request failed with status code:", response.status_code)
except requests.exceptions.RequestException as e:
    print("HTTP request error:", e)
