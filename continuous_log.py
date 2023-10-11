import urllib.request, urllib.parse, urllib.error
import http.client
import base64
import json
import os
from datetime import datetime
import time

# Settings:
repeats = 360
frequency = 30 # Sample every 30 seconds
output_dir = "logging"




def sample(params, headers):
    file_name = datetime.now().strftime("%d%m%Y_%H:%M:%S") + ".json"

    # Submit the HTTP request:
    try:
        conn = http.client.HTTPSConnection('api.wmata.com')
        conn.request("GET", "/TrainPositions/TrainPositions?contentType={contentType}&%s" % params, "{body}", headers)
        response = conn.getresponse()
        data_raw = response.read()
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    # Decode data into JSON object:
    data_string = data_raw.decode('utf8')
    data_json = json.loads(data_string)

    # Dump to JSON file:
    output_file = os.path.join(output_dir, file_name)
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(data_json, outfile, ensure_ascii=False, indent=4)

    print("Successfully wrote response to: " + output_file)


def main():
    # Open the supplied primary api key file:
    with open("primary_api_key","r") as f:
        api_key = f.readline()

    headers = {
        'api_key': api_key,
    }

    params = urllib.parse.urlencode({
    })

    if not os.path.exists('logging'):
        os.makedirs('logging')

    # TODO This is a janky way to achieve 30-second samples:
    for i in range(0,repeats):
        start_time = time.time()
        sample(params, headers)
        dt = time.time() - start_time

        if (i == repeats-1):
            break

        time.sleep(frequency - dt)


if __name__ == "__main__":
    main()