#When given a specific geographical location, this API finds public transport stops, stations, wharfs and points of interest around that location.

from urllib.parse import urlencode
import requests
import json
from pprint import pprint

api_key = ""

base_url = "https://api.transport.nsw.gov.au/v1/tp/"
query_type = "coord?"

#initialise query param dictionary
qdict = {}
#add parameters
qdict["outputFormat"] = "rapidJSON"
qdict["coord"] = "151.2:-33.9:EPSG:4326"
qdict["coordOutputFormat"] = "EPSG:4326"
qdict["inclFilter"] = 1
qdict["type_1"] = "GIS_POINT"
qdict["radius_1"] =1000
qdict["inclDrawClasses_1"] = ""
qdict["type_2"] = "BUS_POINT"
qdict["radius_2"] =1000
qdict["inclDrawClasses_2"] = ""
qdict["type_3"] = "POI_POINT"
qdict["radius_3"] =1000
qdict["inclDrawClasses_3"] = ""
qdict["purpose"] = ""

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
pprint(respdict)