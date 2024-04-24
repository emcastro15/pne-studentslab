import http.server
import socketserver
import termcolor
from pathlib import Path

# -- Server network parameters
PORT = 8080
ERROR_HTML = "html/error.html"
INDEX_HTML = "html/index.html"

socketserver.TCPServer.allow_reuse_address = True


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Message to send back to the client
        resource = self.requestline.split(" ")[1]
        if resource == "/" or resource == "/index.html":
            contents = Path(INDEX_HTML).read_text()
        else:
            html_request = f"html{resource}"
            html_path = Path(html_request)
            try:
                contents = html_path.read_text()
            except FileNotFoundError:
                contents = Path(ERROR_HTML).read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

        return


# -------------- MAIN PROGRAM
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
