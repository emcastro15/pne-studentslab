import http.client
import json

SERVER = 'rest.ensembl.org'
ENDPOINT = '/info/ping'
PARAMS = '?content-type=application/json'
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/) we can also request "/listusers"
try:
    conn.request("GET", '/info/ping?content-type=application/json')
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# Read the response's body
data1 = r1.read().decode("utf-8")

# Parse the JSON response
response = json.loads(data1)

# -- Print the received data
print(f"CONTENT: {data1}")

# Check if the 'ping' property is equal to 1
if 'ping' in response and response['ping'] == 1:
    print("PING OK! The database is running")
else:
    print("ERROR! The database is not running")
