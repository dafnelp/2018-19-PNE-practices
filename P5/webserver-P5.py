import http.server
import socketserver
# Server's port
PORT = 8002


# Class with our handler
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """ Method that is called whenever the GET method is invoked
        in the HTTP protocol request"""

        print("GET received")

        # Print the request line of the client
        print("Request line:" + self.requestline)

        # Print the command received
        print(" Cmd: " + self.command)

        # Print the resource received (the path)
        print(" Path: " + self.path)

        def process_info(f):
            """ Process the info introduced by the client request.
            Parameters:  f: file that should be open depending the request"""

            with open(f, "r") as f:
                content = f.read()

            # Generating the response message
            self.send_response(200)  # --- status line - everything Ok

            # Define the content-type header:
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(content)))

            # The header is finished
            self.end_headers()

            # Send the response message
            self.wfile.write(str.encode(content))

            return

        def process_error(f):
            """ Process the info introduced by the client request (only if
            the request does not exists).
            Parameters:  f: file that should be open depending the request"""

            with open(f, "r") as f:
                content = f.read()

            # Generating the response message
            self.send_response(404)  # --- status line - file not found error

            # Define the content-type header:
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(str.encode(content)))

            # The header is finished
            self.end_headers()

            # Send the response message
            self.wfile.write(str.encode(content))

        # Possible requests of the client

        if "/ HTTP/1.1" in self.requestline:
            process_info("index.html")

        elif "/blue" in self.path:
            process_info("blue.html")

        elif "/pink" in self.path:
            process_info("pink.html")

        else:
            process_error("error.html")

# MAIN PROGRAM

# Set the new handler
Handler = TestHandler

# Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # Main loop: Attend the client. Whenever there is a new
    # client, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")
