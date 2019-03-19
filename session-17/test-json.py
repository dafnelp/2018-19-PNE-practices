import json
import termcolor

f = open("person.json", 'r')

person = json.load(f)

print()

for i, per in enumerate(person["Firstname"]):
    termcolor.cprint("Name {}: ".format(i), 'yellow', end='')
    print(per)
print()
for i, age in enumerate(person["Age"]):
    termcolor.cprint("Age {}: ".format(i), 'blue', end='')
    print(age)
print()
for i, per in enumerate(person["Lastname"]):
    termcolor.cprint("Last name {}: ".format(i), 'green', end='')
    print(per)
print()
for i, num in enumerate(person["phoneNumber"]):
    termcolor.cprint(" Phone {}".format(i), end='')
    termcolor.cprint("   Type:", 'red', end='')
    print(num['type'])
    termcolor.cprint("   Number:", 'red', end='')
    print(num["number"])
