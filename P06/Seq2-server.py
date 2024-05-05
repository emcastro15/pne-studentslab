import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
from Seq1 import *
import jinja2 as j

sequences = ["ATCGATCGAT", "CGATCGATCG", "GATCGATCGA", "ATCGATCGTA", "TCGATCGATC"]
gene_files = {
    'U5': '../sequences/U5.txt',
    'ADA': '../sequences/ADA.txt',
    'FRAT1': '../sequences/FRAT1.txt',
    'FXN': '../sequences/FXN.txt',
    'RNU6_269P': '../sequences/RNU6_269P.txt'
}


def read_html_file(filename):
    contents = Path(filename).read_text()
    contents = j.Template(contents)
    return contents


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
        if resource == "/":
            contents = Path('html/index.html').read_text()
        elif resource.startswith("/ping"):
            contents = Path('html/ping.html').read_text()
        elif resource.startswith("/get"):
            query = urlparse(self.path).query
            params = parse_qs(query)
            number = params.get('n', [''])[0]
            sequence = sequences[int(number)]
            contents = read_html_file("html/get.html").render(context={"number": number, "sequence": sequence})
        elif resource.startswith("/gene"):
            query = urlparse(self.path).query
            params = parse_qs(query)
            gene_name = params.get('gene_name', [''])[0]
            if gene_name in gene_files:
                s1 = Seq()
                sequence = s1.read_fasta(gene_files[gene_name])
                print(sequence)
            else:
                sequence = f"Invalid gene name: {gene_name}"
            contents = read_html_file("html/gene.html").render(context={"gene_name": gene_name, "sequence": sequence})

        else:
            # Server error page
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

"""while True:
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print("Server stopped by the user")
        ls.close()
        exit()

    else:
        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        if msg.startswith('PING'):
            print("PING command")
            response = "OK!\n"
            cs.send(response.encode())
            print(response)
        elif msg.startswith('GET'):
            print("GET command")
            num = int(msg.split(" ")[1])
            if 0 <= num <= 4:
                response = sequences[num]
            else:
                response = "Invalid number! Number should be between 0 and 4."
            cs.send(response.encode())
            print(response)
        elif msg.startswith('INFO'):
            print("INFO command")
            sequence = msg.split(" ")[1]
            s1 = Seq(sequence)
            bases_length = s1.len()
            bases_count = s1.count()
            response = f"Sequence: {sequence}\nTotal length: {bases_length}\n"
            for key, value in bases_count.items():
                percentage = round((value / bases_length) * 100, 1)
                response += f"{key}: {value} ({percentage}%)\n"
            cs.send(response.encode())
            print(response)
        elif msg.startswith('COMP'):
            print("COMP command")
            sequence = msg.split(" ")[1]
            s1 = Seq(sequence)
            response = s1.complement()
            cs.send(response.encode())
            print(response)
        elif msg.startswith('REV'):
            print("REV command")
            sequence = msg.split(" ")[1]
            s1 = Seq(sequence)
            response = s1.reverse()
            cs.send(response.encode())
            print(response)
        elif msg.startswith('GENE'):
            print("GENE command")
            gene_name = msg.split(" ")[1]
            if gene_name in gene_files:
                s1 = Seq()
                response = s1.read_fasta(gene_files[gene_name])
            else:
                response = f"Invalid gene name: {gene_name}"
            cs.send(response.encode())
            print(response)
        cs.close()"""
