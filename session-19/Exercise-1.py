import http.client
import json
import termcolor


def process_info(ENDPOINT):

    HOSTNAME = "api.icndb.com"
    METHOD = "GET"

    # -- Here we can define special headers if needed
    headers = {'User-Agent': 'http-client'}

    # -- Connect to the server
    # -- NOTICE it is an HTTPS connection!
    # -- If we do not specify the port, the standard one
    # -- will be used
    conn = http.client.HTTPSConnection(HOSTNAME)
    # -- Send the request. No body (None)
    # -- Use the defined headers
    conn.request(METHOD, ENDPOINT, None, headers)

    # -- Wait for the server's response
    r1 = conn.getresponse()

    # -- Print the status
    print()
    print("Response received: ", end='')
    print(r1.status, r1.reason)
    print()

    # -- Read the response's body and close
    # -- the connection
    text_json = r1.read().decode("utf-8")
    conn.close()

    # -- Generate the object from the json file
    jokes = json.loads(text_json)

    # Performing the operations depending the ENDPOINT

    # NUMBER OF TOTAL JOKES
    if ENDPOINT == "/jokes/count":
        number_jokes = jokes["value"]

        termcolor.cprint("The total number of jokes about Chuck Norris is:", 'blue')
        print(number_jokes)

    # NUMBER AND NAME OF THE CATEGORIES
    elif ENDPOINT == "/categories":
        name_categories = jokes["value"]
        number_categories = len(name_categories)

        termcolor.cprint("The different categories of jokes are:", 'green')
        print(name_categories)

        termcolor.cprint("The number of different categories is:", 'green')
        print(number_categories)

    # RANDOM JOKE
    elif ENDPOINT == "/jokes/random":
        random_joke = jokes["value"]["joke"]
        termcolor.cprint("A random joke about Chuck Norris:", 'red')
        print(random_joke)

# Calling the functions to print the information every time we execute the program


process_info("/jokes/count")
process_info("/categories")
process_info("/jokes/random")
