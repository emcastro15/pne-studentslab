import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import http.client
import json
import jinja2 as j
from Seq1 import *


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
    species_encoded = species.replace(' ', '%20')
    SERVER = 'rest.ensembl.org'
    ENDPOINT = f'/info/assembly/{species_encoded}'
    PARAMS = '?content-type=application/json'
    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", ENDPOINT + PARAMS)
    r1 = conn.getresponse()
    if r1.status != 200:
        return None
    data1 = r1.read().decode("utf-8")
    response = json.loads(data1)
    print(response)
    karyotype = response.get('karyotype', [])
    return karyotype


def get_chromosome_length(species, chromo):
    species_encoded = species.replace(' ', '%20')
    SERVER = 'rest.ensembl.org'
    ENDPOINT = f'/info/assembly/{species_encoded}'
    PARAMS = '?content-type=application/json'
    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", ENDPOINT + PARAMS)
    r1 = conn.getresponse()
    if r1.status != 200:
        return None
    data1 = r1.read().decode("utf-8")
    response = json.loads(data1)
    chromosomes = response.get('top_level_region', [])
    for chromosome in chromosomes:
        if chromosome['name'] == chromo:
            return chromosome['length']
    return None


def get_gene_id(gene):
    SERVER = 'rest.ensembl.org'
    ENDPOINT = f'/lookup/symbol/homo_sapiens/{gene}'
    PARAMS = '?expand=1;content-type=application/json'
    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", ENDPOINT + PARAMS)
    r1 = conn.getresponse()
    if r1.status != 200:
        return None
    data1 = r1.read().decode("utf-8")
    response = json.loads(data1)
    if 'error' in response:
        return None
    gene_id = response['id']
    return gene_id


def get_gene_sequence(gene_id):
    # Now we get the sequence using the gene ID
    SERVER = 'rest.ensembl.org'
    SEQ_ENDPOINT = f'/sequence/id/{gene_id}'
    SEQ_PARAMS = '?content-type=application/json'
    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", SEQ_ENDPOINT + SEQ_PARAMS )
    r2 = conn.getresponse()
    if r2.status != 200:
        return None
    data2 = r2.read().decode("utf-8")
    sequence_response = json.loads(data2)
    sequence = sequence_response.get('seq', None)
    return sequence


def get_gene_info(gene):
    SERVER = 'rest.ensembl.org'
    ENDPOINT = f'/lookup/symbol/homo_sapiens/{gene}'
    PARAMS = '?expand=1;content-type=application/json'
    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", ENDPOINT + PARAMS)
    r1 = conn.getresponse()
    if r1.status != 200:
        return None
    data1 = r1.read().decode("utf-8")
    response = json.loads(data1)
    if 'error' in response:
        return None
    gene_id = response['id']
    start = response['start']
    end = response['end']
    length = response['end'] - response['start'] + 1
    name = response['display_name']
    return gene_id, start, end, length, name


def calculate_gene_info(sequence):
    # Use Seq class methods to perform calculations
    length = sequence.len()
    count_bases = sequence.count()
    percentages = {}
    for base, count in count_bases.items():
        percentages[base] = f"{(count / length) * 100}%"
    return length, percentages


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
        params = parse_qs(query, keep_blank_values=True)

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
            print(species)
            karyotype = get_karyotype(species)
            if karyotype is None:
                contents = Path('html/error.html').read_text()
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
        elif resource.startswith("/chromosomeLength"):
            species = params.get('species', [''])[0]
            chromo = params.get('chromo', [''])[0]
            length = get_chromosome_length(species, chromo)
            if length is None:
                contents = Path('html/error.html').read_text()
            else:
                chromosome_length = f"The length of chromosome '{chromo}' for species '{species}' is {length}."
                contents = read_html_file('html/chromosomeLength.html').render(
                    context={
                        "chromosome_length": chromosome_length
                    }
                )
        elif resource.startswith("/geneSeq"):
            gene = params.get('gene', [''])[0]
            gene_id = get_gene_id(gene)
            sequence = get_gene_sequence(gene_id)
            if sequence is None:
                contents = Path('html/error.html').read_text()
            else:
                contents = read_html_file('html/geneSeq.html').render(
                    context={
                        "gene": gene,
                        "sequence": sequence
                    }
                )
        elif resource.startswith("/geneInfo"):
            gene = params.get('gene', [''])[0]
            gene_id, start, end, length, name = get_gene_info(gene)
            if gene_id is None:
                contents = Path('html/error.html').read_text()
            else:
                contents = read_html_file('html/geneInfo.html').render(
                    context={
                        "name": name,
                        "gene_id": gene_id,
                        "start": start,
                        "end": end,
                        "length": length,
                    }
                )
        elif resource.startswith("/geneCalc"):
            gene = params.get('gene', [''])[0]
            gene_id = get_gene_id(gene)
            sequence = get_gene_sequence(gene_id)
            if sequence is None:
                contents = Path('html/error.html').read_text()
            else:
                # Perform calculations using Seq class methods
                seq_obj = Seq(sequence)
                length, percentages = calculate_gene_info(seq_obj)
                contents = read_html_file('html/geneCalc.html').render(
                    context={
                        "gene": gene,
                        "length": length,
                        "percentages": percentages
                    }
                )
        else:
            contents = Path('html/error.html').read_text()

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