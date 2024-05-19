import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import http.client
import json
import jinja2 as j


def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents


def get_species(limit=None):
    SERVER = 'rest.ensembl.org'
    ENDPOINT = '/info/species'
    PARAMS = '?content-type=application/json'
    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", ENDPOINT + PARAMS)
    r1 = conn.getresponse()
    if r1.status != 200:
        return []
    data1 = r1.read().decode("utf-8")
    response = json.loads(data1)
    species_list = [species['display_name'] for species in response['species']]
    all_species = species_list
    if limit:
        species_list = species_list[:limit]
    return species_list, all_species


def get_karyotype(species):
    SERVER = 'rest.ensembl.org'
    ENDPOINT = f'/info/assembly/{species}'
    PARAMS = '?content-type=application/json'
    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", ENDPOINT + PARAMS)
    r1 = conn.getresponse()
    if r1.status != 200:
        return None
    data1 = r1.read().decode("utf-8")
    response = json.loads(data1)
    karyotype = response.get('karyotype', [])
    return karyotype


# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        resource = urlparse(self.path).path
        query = urlparse(self.path).query
        params = parse_qs(query)

        if resource == "/":
            contents = Path('html/index.html').read_text()
        elif resource.startswith("/listSpecies"):
            limit = params.get('limit', [None])[0]
            try:
                limit = int(limit)
            except ValueError:
                limit = None
            except TypeError:
                limit = None
            species_list, all_species = get_species(limit)
            html_species_list = ""
            for species in species_list:
                html_species_list += f"- {species}\n"
            contents = read_html_file('html/listSpecies.html').render(
                context={
                    "list": html_species_list,
                    "total_species": len(all_species),
                    "limit": limit
                }
            )
        elif resource.startswith("/karyotype"):
            species = params.get('species', [''])[0]
            karyotype = get_karyotype(species)
            if karyotype is None:
                contents = f"species '{species}' not found."
            else:
                html_karyotype_list = ""
                for chromosome in karyotype:
                    html_karyotype_list += f"- {chromosome}\n"
                contents = read_html_file('html/karyotype.html').render(
                    context={
                        "species": species,
                        "karyotype_list": html_karyotype_list
                    }
                )
        else:
            contents = Path('html/error.html')
        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()
