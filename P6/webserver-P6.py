import http.server
import socketserver
import termcolor

from Seq import Seq

# Define the port
PORT = 8001


# Class with our handler
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Printing the request line
        termcolor.cprint(self.requestline, 'green')

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

            return

        # Open the main page
        if "/ HTTP/1.1" in self.requestline:
            process_info("index.html")

        # Open the page with the message introduced by the client
        elif "/seq" in self.path:
            msg = self.requestline.split()
            # Position in the request line that correspond to the echo message
            position = msg[1]
            # Way to have the message of the client
            msg_cl = position.find("msg=")
            msg_end = position.find("&")
            # ---- MESSAGE OF THE CLIENT ----
            seq_msg = position[msg_cl + 4: msg_end]
            seq_msg = seq_msg.upper()

            invalid_char = False
            for letter in seq_msg:
                letter = letter.upper()
                if letter != 'A' and letter != 'C' and letter != 'G' and letter != 'T':
                    invalid_char = True

            if invalid_char:
                process_error("error.html")

            else:
                if "chk" in self.path:
                    seq_dna = Seq(seq_msg)
                    len_seq = seq_dna.len()
                    seq_len = str(len_seq)

                    contents = """
                        <!DOCTYPE html>
                        <html lang="en" dir="ltr">
                          <head>
                            <meta charset="utf-8">
                            <title>DNA SEQUENCE</title>
                          </head>
                          <body style="background-color: lightblue;">
                            <h1>DNA SEQUENCE</h1>
                             <br>""" + seq_msg + """ <br><br>
                             <br>""" + seq_len + """ <br><br>
                            <a href="10.0.2.15:8000/">Link to main server</a>
                          </body>
                        </html>
                        """

                else:
                    contents = """
                        <!DOCTYPE html>
                        <html lang="en" dir="ltr">
                          <head>
                            <meta charset="utf-8">
                            <title>DNA SEQUENCE</title>
                          </head>
                          <body style="background-color: lightblue;">
                            <h1>DNA SEQUENCE</h1>
                             <br>""" + seq_msg + """ <br><br>
                            <a href="10.0.2.15:8000/">Link to main server</a>
                          </body>
                        </html>
                        """

                # Everything is OK
                status_line = "HTTP/1.1 200 OK\r\n"

                # Build the header
                header = "Content-Type: text/html\r\n"
                header += "Content-Length: {}\r\n".format(len(str.encode(contents)))

                # Build the message by joining together all the parts
                response_msg = str.encode(status_line + header + "\r\n" + contents)

                # Send the echo message
                self.wfile.write(response_msg)

        # Error page
        else:
            process_error("error.html")


# MAIN PROGRAM

with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- client, the handler is called
    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()

print("")
print("Server Stopped")
