import http.server
import socketserver
import termcolor

# Define the port
PORT = 8000

# Class with our handler
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Printing the request line
        termcolor.cprint(self.requestline, 'green')
        # Contents of the HTML file
        f = open("form2.html", 'r')
        contents = f.read()
        # Send the response
        self.send_response(200)  # Everything OK
        # Define the content-type header
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # Close the headers
        self.end_headers()

        # Sending the body of the response message
        self.wfile.write(str.encode(contents))


# MAIN PROGRAM

with socketserver.TCPServer(("", PORT), TestHandler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")