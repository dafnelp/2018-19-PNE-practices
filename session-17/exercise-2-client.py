# -- Example of a client that uses the HTTP.client library
# -- for requesting the main page from the server
import http.client
import termcolor
import json

PORT = 8001
SERVER = 'localhost'

print("\nConnecting to server: {}:{}\n".format(SERVER, PORT))

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
conn.request("GET", "/listusers")

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print("Response received!: {} {}\n".format(r1.status, r1.reason))

# -- Read the response's body
data1 = r1.read().decode("utf-8")

print("CONTENT: ")

# -- Print the received data
print(data1)

# -- Create a variable with the data,
# -- form the JSON received
person = json.loads(data1)

print("CONTENT: ")

print()
person_info = len(person['Firstname'])

for i in range(person_info):
    termcolor.cprint("Name {}:".format(i), 'blue', end="")
    print()
    # The first name and the last name of the person
    termcolor.cprint("    First name: ", 'red', end='')
    print(person["Firstname"][i])
    termcolor.cprint("    Last name: ", 'red', end='')
    print(person["Lastname"][i])

    # The age of the person
    termcolor.cprint("    Age: ", 'green', end='')
    print(person["Age"][i])

    # Get the phoneNumber list
    phoneNumbers = person['phoneNumber'][i]

    # Print the number of elements int the list
    termcolor.cprint("Phone numbers: ", 'yellow', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("   Phone {}:".format(i), 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("     Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("     Number: ", 'red', end='')
        print(num['number'])
