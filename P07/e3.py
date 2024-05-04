import http.client
import json
import termcolor
from e2 import genes

SERVER = 'rest.ensembl.org'
ENDPOINT = f'/sequence/id/{genes["MIR633"]}' # ENSG00000207552
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
    conn.request("GET", ENDPOINT + PARAMS)
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


termcolor.cprint("Gene:", 'green', end="")
print("MIR633")
termcolor.cprint("Description:", 'green', end="")
print(response['desc'])
termcolor.cprint("Bases:", 'green', end="")
print(response['seq'])
