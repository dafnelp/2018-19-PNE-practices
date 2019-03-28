import http.client
import json

# WAY TO KNOW THE WOEID OF THE CITY
valid_city = True
while valid_city:
    # If the city introduced it is not valid and therefore the
    # woeid, the program keep asking
    city = input("Introduce a city: ")
    city = city.lower()

    if len(city) == 0:
        continue

    else:
        valid_city = False

        # -- API information
        HOSTNAME = "www.metaweather.com"
        ENDPOINT = "/api/location/search/?query=" + city
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

        # -- Read the response's body and close
        # -- the connection
        text_json = r1.read().decode("utf-8")
        conn.close()

        # -- Generate the object from the json file
        info_city = json.loads(text_json)

        # Woeid of the introduced city
        woeid = info_city[0]["woeid"]
        woeid = str(woeid)

        # INFO OF THE CITY INTRODUCED (ALREADY KNOWING THE WOEID)

        # -- API information
        HOSTNAME = "www.metaweather.com"
        ENDPOINT = "/api/location/"
        METHOD = "GET"

        # -- Here we can define special headers if needed
        headers = {'User-Agent': 'http-client'}

        # -- Connect to the server
        # -- NOTICE it is an HTTPS connection!
        # -- If we do not specify the port, the standarD one
        # -- will be used
        conn = http.client.HTTPSConnection(HOSTNAME)

        # -- Send the request. No body (None)
        # -- Use the defined headers
        conn.request(METHOD, ENDPOINT + woeid + '/', None, headers)

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
        weather = json.loads(text_json)

        # -- Get the data
        time = weather['time']

        temp0 = weather['consolidated_weather'][0]
        description = temp0['weather_state_name']
        temp = temp0['the_temp']
        place = weather['title']
        sunset = weather['sun_set']

        print()
        print("Place: {}".format(place))
        print("Time: {}".format(time))
        print("Weather description: {}".format(description))
        print("Current temp: {} degrees".format(temp))
        print("Sunset at: {} ".format(sunset))


