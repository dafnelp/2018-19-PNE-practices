import http.client
import termcolor
import json

from Seq import Seq

# Connect with the complete API Rest from ensembl
conn = http.client.HTTPConnection('rest.ensembl.org')

# -- Send the request message, using the GET method. We are
# -- requesting a sequence (/sequence/id), an Ensembl stable ID
# -- (ENSG00000165879) and changing the content-type since we are using json
conn.request("GET", "/sequence/id/ENSG00000165879?content-type=application/json")

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
gen_info = json.loads(data1)

# Accessing the sequence like in a dictionary
FRAT1_gen = gen_info['seq']

# Using the Class Seq
FRAT1_gen = Seq(FRAT1_gen)

# -- LENGTH OF THE GEN --
len_gen = FRAT1_gen.len()
termcolor.cprint("The total number of bases are: ", 'blue')
print(len_gen)

# -- COUNT T BASES --
bases_t = FRAT1_gen.count_bases("T")
termcolor.cprint("The number of T bases are: ", 'yellow')
print(bases_t)



# -- PERCENTAGE OF ALL BASES --
bases = ["A", "C", "T", "G"]
for i in bases:
    bases_percentage = FRAT1_gen.perc(i)
    termcolor.cprint("Percentage: ", 'green')
    print(bases_percentage)
