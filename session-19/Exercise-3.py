import http.client
import json


def connection(ENDPOINT):
    """Function that allow the connection to the server.
    Parameters: ENDPOINT --- different endpoints depending the different
     resources provided by the server"""

    # -- API information
    HOSTNAME = "api.github.com"
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

    # -- Read the response's body and close
    # -- the connection
    text_json = r1.read().decode("utf-8")
    conn.close()

    # -- Generate the object from the json file
    return json.loads(text_json)

# Name of the GitHub users we want to know the info
GITHUB_ID = input("Introduce the name of a GitHub user:")

# Use the function in order to return information about the users
user = connection('/users/' + GITHUB_ID)

# -- Get some data
name = user['name']
nrepos = user['public_repos']

print()
print("Name: {}".format(name))
print("Repos: {}".format(nrepos))

# Use the function in order to return information about the repos
repos = connection('/users/' + GITHUB_ID + '/repos')
for i, repo in enumerate(repos):
    print()
    print("{} Repo: {}".format(i, repo['name']))

# Use the function in order to return information about the 2018-19-PNE-practices repo
commits = connection('/repos/' + GITHUB_ID + '/2018-19-PNE-practices/commits')
# -- Get some data
total_commits = commits
print()
print("The total commits to 2018-19-PNE-practices repo are: {}".format(len(total_commits)))
