from urllib.parse import urlencode
import requests
import json
import tssetup
from pprint import pprint

api_key = tssetup.getKey()

base_url = "https://api.transport.nsw.gov.au/v1/tp/"
query_type = "trip?"

#initialise query param dictionary
qdict = {}
#add parameters
qdict["outputFormat"] = "rapidJSON"
qdict["coordOutputFormat"] = "EPSG:4326"
qdict["depArrMacro"] = "dep" #dep after or arr before
qdict["itdDate"] = "20170707"
qdict["itdTime"] = "1200"
qdict["type_origin"] = "any"
qdict["name_origin"] = "10101331" #get location/stop id from stop_finder.py
qdict["type_destination"] = "any"
qdict["name_destination"] = "10102027"
qdict["calcNumberOfTrips"] = 5
qdict["wheelchair"] = "" #or "on"
qdict["TfNSWSF"] = "true"
qdict["version"] = "10.2.1.15"

#encode params as querystring
qstring = urlencode(qdict)

#buildurl
urlsend = base_url + query_type + qstring
print(urlsend)

#get authentication
headers = {'Authorization': 'apikey ' + api_key, 'Accept': 'application/json'}
response = requests.get(urlsend, headers=headers)

#decode response and convert to JSON format
respdict = json.loads(response.content.decode('utf-8'))


#simple example to look at data

for x in range(len(respdict["journeys"])):
    print("*********  TRIP " + str(x+1) + "  *********")

    for y in range(len(respdict["journeys"][x]["legs"])):

        print("LEG " + str(y+1) + "")
        print("Duration " + str(respdict["journeys"][x]["legs"][y]["duration"]/60) + " mins", end="\n")

        print(respdict["journeys"][x]["legs"][y]["origin"]["departureTimeEstimated"], end="\t")
        print(respdict["journeys"][x]["legs"][y]["origin"]["name"], end="\n")
        print(respdict["journeys"][x]["legs"][y]["destination"]["arrivalTimeEstimated"], end="\t")
        print(respdict["journeys"][x]["legs"][y]["destination"]["name"], end="\n")
        print("\t\t")



