import json
import termcolor

# -- Open the json file
f = open("person.json", 'r')

# Read the data from the file
# Now person is a dictionary with all the information
person = json.load(f)

# Print the information in the object
print()
person_info = len(person['Firstname'])
print("Total people in the data base: {}".format(person_info))

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
