import urllib.request, urllib.parse, urllib.error
import http.client
import base64
import json

# Open the supplied primary api key file:
with open("primary_api_key","r") as f:
    api_key = f.readline()



headers = {
    'api_key': api_key,
}

params = urllib.parse.urlencode({
})



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
with open('output_positions.json', 'w', encoding='utf-8') as outfile:
    json.dump(data_json, outfile, ensure_ascii=False, indent=4)


try:
    conn = http.client.HTTPSConnection('api.wmata.com')
    conn.request("GET", "/TrainPositions/StandardRoutes?contentType={contentType}&%s" % params, "{body}", headers)
    response = conn.getresponse()
    data_raw = response.read()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

data_string = data_raw.decode('utf-8')
data_json = json.loads(data_string)

with open('output_standard_routes.json', 'w', encoding='utf-8') as outfile:
    json.dump(data_json, outfile, ensure_ascii=False, indent=4)