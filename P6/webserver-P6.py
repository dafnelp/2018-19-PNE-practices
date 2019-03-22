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

        def valid_seq(seq_msg):
            """Function to know if the characters introduced by the
            client are a sequence of DNA.
            Parameters: seq_msg that corresponds to the message introduced
            by the client"""

            for letter in seq_msg:
                # Way that allow to recognize upper and lower introduced characters
                letter = letter.upper()
                if letter != 'A' and letter != 'C' and letter != 'G' and letter != 'T':
                    # Open the error HTML file
                    process_error("error.html")
                    return False
            return True

        def chk_len(seq_dna):
            """Function that gives the length of the sequence if the
            client have selected the check button.
            Parameters: seq_dna --- seq_msg already converted into the
            Class Seq"""

            if "chk" in self.path:
                len_seq = "Total length of the sequence: {}".format(seq_dna.len())
                return len_seq
            return "Check button have not been selected"

        def treat(seq_dna, operation, base):
            """Function that performs the count or the percentage of the bases.
            Parameters: seq_dna --- seq_msg already converted into the
            Class Seq, operation --- count or percentage, base --- type of base of DNA"""

            if operation == "count":
                if base == "A":
                    counter_bases_A = "Number of bases {}".format(seq_dna.count_bases("A"))

                    return counter_bases_A

                elif base == "C":
                    counter_bases_C = "Number of bases {}".format(seq_dna.count_bases("C"))

                    return counter_bases_C

                elif base == "T":
                    counter_bases_T = "Number of bases {}".format(seq_dna.count_bases("T"))

                    return counter_bases_T

                elif base == "G":
                    counter_bases_G = "Number of bases {}".format(seq_dna.count_bases("G"))

                    return counter_bases_G

            elif operation == "perc":
                if base == "A":
                    perc_A = "Percentage of {}".format(seq_dna.perc("A"))

                    return perc_A

                elif base == "C":
                    perc_C = "Percentage of {}".format(seq_dna.perc("C"))

                    return perc_C

                elif base == "T":
                    perc_T = "Percentage of {}".format(seq_dna.perc("T"))

                    return perc_T

                elif base == "G":
                    perc_G = "Percentage of {}".format(seq_dna.perc("G"))

                    return perc_G

        def process_client(msg):
            """Function that process the request of the client and
            opens thee new page"""

            # Processing the request message
            msg = self.requestline.split()
            # Position in the request line that correspond to the sequence
            position = msg[1]
            # Way to have the message of the client
            msg_cl = position.find("msg=")
            msg_end = position.find("&")
            # Way to know the base to perform the operations
            base_start = position.find("base")
            base_end = position.find("&operation")
            # Way to know the operation
            oper_start = position.find("operation")

            # ---- MESSAGE OF THE CLIENT ----
            seq_msg = position[msg_cl + 4: msg_end]
            seq_msg = seq_msg.upper()

            # ---- BASE ----
            base = position[base_start + 5: base_end]

            # ---- OPERATION ----
            operation = position[oper_start + 10:]

            # Using the Class Seq
            seq_dna = Seq(seq_msg)

            # ---- CALLING THE FUNCTIONS ----
            valid_seq(seq_msg)
            chk_len(seq_dna)
            treat(seq_dna, operation, base)

            # Naming the functions and converting them to strings in order to using
            # them in the HTML

            length = str(chk_len(seq_dna))
            operations = str(treat(seq_dna, operation, base))

            # --- VALID SEQUENCE INTRODUCED ---

            if valid_seq(seq_msg):
                # Creating the HTML
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
                         <br>""" + length + """ <br><br>
                         <br>""" + operations + """ <br><br>
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

                # Send the message
                self.wfile.write(response_msg)

        # Open the main page
        if "/ HTTP/1.1" in self.requestline:
            process_info("index.html")

        # Open the page with the message according the request
        elif "/seq" in self.path:
            process_client(msg=self.requestline)

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
