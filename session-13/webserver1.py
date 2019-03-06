import http.server
import socketserver
# Server's port
PORT = 8001


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

        # Path requested by the client
        if self.path == "/":

            # Open the file
            with open("index.html", "r") as f:
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

        else:
            # Open the file
            with open("error.html", "r") as f:
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

        return

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
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")
