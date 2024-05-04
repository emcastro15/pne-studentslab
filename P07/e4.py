import http.client
import json
import termcolor
from genes_dict import genes
from Seq1 import *

gene_name = input("Write the gene name:")

SERVER = 'rest.ensembl.org'
ENDPOINT = f'/sequence/id/{genes[gene_name]}'
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


termcolor.cprint("Gene: ", 'green', end="")
print(gene_name)
termcolor.cprint("Description: ", 'green', end="")
print(response['desc'])

seq = response['seq']
s1 = Seq(seq)
termcolor.cprint("Total length: ", 'green', end="")
print(s1.len())
bases_count = s1.count()
print(bases_count)
for base, count in bases_count.items():
    percentage = round((count / s1.len()) * 100, 1)
    termcolor.cprint(base, 'blue', end="")
    print(f": {count} ({percentage}%)")
termcolor.cprint("Most frequent base: ", 'green', end="")
print(most_frequent_base(bases_count))
