from urllib.parse import urlencode
import requests
import json

api_key = ""

base_url = "https://api.transport.nsw.gov.au/v1/tp/"
query_type = "stop_finder?"

#initialise query param dictionary
qdict = {}
#add parameters
qdict["outputFormat"] = "rapidJSON"
qdict["type_sf"] = "any"
qdict["name_sf"] = "St Peters"
qdict["coordOutputFormat"] = "EPSG:4326"
qdict["anyMaxSizeHitList"] = 5
qdict["TfNSWSF"] = "true"
qdict["version"] = "10.2.1.15"

#encode params as querystring
qstring = urlencode(qdict)

#buildurl
urlsend = base_url + query_type + qstring

#get authentication
headers = {'Authorization': 'apikey ' + api_key, 'Accept': 'application/json'}
response = requests.get(urlsend, headers=headers)

#decode response and convert to JSON format
respdict = json.loads(response.content.decode('utf-8'))

#simple example to look at data
for x in respdict['locations']:
    print(x['name'] + "\t" + str(x['id']))