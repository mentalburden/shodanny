#!/usr/bin/python3
#Runs a shodan lookup for each unique ip in the apache access logs (or whatever other log)
#Ships info to firebase (realtime db) with an unauthed curl (will add token'ing later on, maybe)
#Visualize hits with GeoFire/Gmaps API to do the funky analytics chicken dance (need airgapped options instead of Googs)
#firebase ship: curl -X PATCH -d '{shodan-junk-here} 'https://your-burner-account's-firebase-project.firebaseio.com/TELEPHONE/testtraffic/ipaddress-cleaned.json'

import re, os, sys, requests, json, time
import shodan
import pprint

filepath = '/var/log/apache2/access.log'
api = shodan.Shodan("A-FanCy-ApI-KEy")
testarray = []
telephone = {"no-shodan-info":"---none---"}
service = 'https://some-kinda-project-oh-jeez-rick-f8299.firebaseio.com'
pp = pprint.PrettyPrinter(indent=3)

def runNudeTayne(hatwobble):
	try:
		hatarray = []
		singlehost = api.host(hatwobble)
		hatorg = singlehost.get('org', 'n/a')
		hatos = singlehost.get('os', 'n/a')
		#for item in singlehost.get('location','n/a'):
		hatcity = singlehost.get('city','n/a')
		hatcountry = singlehost.get('country','n/a')
		hatcountrycode = singlehost.get('country_code','n/a')
		hatisp = singlehost.get('isp','n/a')
		hatasn = singlehost.get('asn','n/a')
		for item in singlehost['data']:
			hatport = str(item['port'])
			hatdata = str(item['data'].encode('utf-8'))
			cleanhatdata = hatdata.replace(":","-") #get rid of :'s in the json port dat
			hatarray.append({"port":hatport,"portinfo":cleanhatdata})
		chonker = {"ip":hatwobble,"org":hatorg,"os":hatos,'city':hatcity,'country':hatcountry,'countrycode':hatcountrycode,'isp':hatisp,'asn':hatasn, "service-data":hatarray}
		time.sleep(1) #Shodan API rate limiter
		return chonker
	except shodan.APIError:
		return telephone

def doTheThing(id):
	cleandata = json.dumps(runNudeTayne(id))
	myurl = service+"/curl/data/"+str(id).replace(".","d")+".json"
	chonker = requests.patch(myurl, data=cleandata)
	thisdata = json.loads(cleandata)
	if len(thisdata) > 1)
		print("#####################################################################")
		print("IP: "+str(thisdata["ip"]))
		print("Org: "+str(thisdata["org"]))
		print("OS: "+str(thisdata["os"]))
		print("ASN: "+str(thisdata["asn"]))
		print("City: "+str(thisdata["city"]))
		print("Country: "+str(thisdata["country"]))
		print("CountryCode: "+str(thisdata["countrycode"]))
		print(str(pp.pprint(thisdata["service-data"])))

def getTheStuff(split_line):
	split_line = line.split()
	return split_line[0]

#main starts here
with open(filepath) as fp:
	line = fp.readline()
	cnt = 1
	while line:
		thisline = getTheStuff(line.strip())
		testarray.append(thisline)
		line = fp.readline()
		cnt += 1
for x in set(testarray):
	doTheThing(x)
