#Provides capability to display all public transport service status and incident information (as published from the Incident Capture System).
from urllib.parse import urlencode
import requests
import json
from pprint import pprint
import tssetup

api_key = tssetup.getKey()

base_url = "https://api.transport.nsw.gov.au/v1/tp/"
query_type = "add_info?"

#initialise query param dictionary
qdict = {}
#add parameters
qdict["outputFormat"] = "rapidJSON"
qdict["filterDateValid"] = "21-04-2017"
qdict["filterMOTType"] = "" #(1,4,5,7,9,11):(Train, LR, Bus, Coach, Ferry, School Bus)
qdict["filterPublicationStatus"] = "current" #current or "" to include historical alerts
qdict["itdLPxx_selStop"] = "" #filter by stop ID e.g. 10111010
qdict["itdLPxx_selLine"] = "020T1" #filter by line no. e.g 020T1
qdict["itdLPxx_selOperator"] = "" #filter by operatorid
qdict["filterPNLineDir"] = "" #filter by route NNN:LLLLL:D, (NNN: subnet, LLLLL: Route number, D: direction H/R).
qdict["filterPNLineSub"] = "" #filter by route NNN:LLLLL:E:D
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
pprint(respdict)