from urllib.parse import urlencode
import requests
import json
import tssetup

api_key = tssetup.getKey()

base_url = "https://api.transport.nsw.gov.au/v1/tp/"
query_type = "departure_mon?"

#initialise query param dictionary
qdict = {}
#add parameters
qdict["outputFormat"] = "rapidJSON"
qdict["coordOutputFormat"] = "EPSG:4326"
qdict["mode"] = "direct"
qdict["type_dm"] = "stop"
qdict["name_dm"] = "10101443" #can search via a string but need to find exactly one stop St P: 10101443, Bus: 10112735
qdict["nameKey_dm"] = "" #can set as $USEPOINTS$ to choose a particular platform
qdict["depArrMacro"] = "dep"
qdict["itdDate"] = "20170421"
qdict["itdTime"] = "2300"
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
for x in respdict["location"]:
    print(x["name"])
for x in respdict["stopEvents"]:
    print(x["departureTimePlanned"], end = ":  ")
    print(x["transportation"]["name"], end = "\t\t")
    print(x["transportation"]["destination"]["name"])