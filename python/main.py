from retriever import retriever
import argparse
from status import status

parser = argparse.ArgumentParser(description='Server Status')
parser.add_argument('-u', '--url', action='store', help='enter url')
parser.add_argument('-p', '--metric', action='store', help='enter metric')
parser.add_argument('-c', '--critical_threshold', action='store', help='enter critical threshold')
parser.add_argument('-w', '--warning_threshold', action='store', help='enter warning threshold')

# Parse Arguments
parsed = parser.parse_args()
url = parsed.url
if(url == None):
	url = "https://play.grafana.org/api/datasources/proxy/1/render?target=aliasByNode(movingAverage(scaleToSeconds(apps.fakesite.*.counters.requests.count,%201),%202),%202)&format=json&from=-5min"
wt = float(parsed.critical_threshold)
ct = float(parsed.warning_threshold)

#Retrieve Data
datapoints = retriever(url = url).retrieveJSON()

#Check Status
statusChecker = status()
for blocks in datapoints:
    for entries in blocks['datapoints']:
        print(statusChecker.check(wt, ct, entries[0]))
    
