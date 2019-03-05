import http.server
import socketserver

PORT = 8001


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET received")

        print("Request line:" + self.requestline)
        print(" Cmd: " + self.command)
        print(" Path: " + self.path)

        content = "I am the happy server! :)"

        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return
# Handler = http.server.SimpleHTTPRequestHandler (another way to do it)
Handler = TestHandler

# LoCAL IP address
with socketserver.TCPServer(("", 8001), Handler) as httpd:
    print("Serving at PORT", PORT)

    httpd.serve_forever()
