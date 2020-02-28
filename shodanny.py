#!/usr/bin/python
import shodan
import argparse
import json
import re, sys, os, time

api = shodan.Shodan("ThAt-api-kEy-tho")
celeryarray = []
jsonname = "jsontest.json" #output file, make this an arg later
apicalllimiter = 2 # less than two secs sometimes triggers their dumbass throttling... -_-

#---------------------------Getting the json file early-

jason = open(jsonname,"ab+")

#---------------------------Funcs start here-

def cleanBaby(stringyboi):
        re.sub(r':', '-', stringyboi)
	re.sub(r',', '-', stringyboi)
        return str(stringyboi.encode('utf-8'))

def runFullQuery(searchyboi):
	try:
        	results = api.search(searchyboi)
	        print('Results found: %s' % results['total'])
	        for result in results['matches']:
	                print(result['ip_str'])
	except shodan.APIError, e:
	        print( 'Error: %s' % e)

def runTayne(hatwobble):
	singlehost = api.host(hatwobble)
	print(hatwobble)
	print(singlehost.get('org', 'n/a'))
	print(singlehost.get('os', 'n/a'))
	for item in singlehost['data']:
		print(item['port'])
		print(item['data'].encode('utf-8'))
	time.sleep(apicalllimiter)


def runNudeTayne(hatwobble):
        hatarray = []
        singlehost = api.host(hatwobble)
        hatorg = singlehost.get('org', 'n/a')
        hatos = singlehost.get('os', 'n/a')
        for item in singlehost['data']:
		hatport = str(item['port'])
                hatdata = str(item['data'].encode('utf-8'))
		cleanhatdata = hatdata.replace(":","-") #get rid of :'s in the json port data
		hatarray.append({"port":hatport,"portinfo":cleanhatdata})
        chonker = {"ip":hatwobble,"org":hatorg,"os":hatos,"service-data":hatarray}
	jason.write(json.dumps(chonker))
        time.sleep(apicalllimiter)


def runCeleryMan(tayne):
        try:
                results = api.search(tayne)
                print('Results found: %s' % results['total'])
                for result in results['matches']:
                        celeryarray.append((result['ip_str'].encode('utf-8')))
        except shodan.APIError, e:
                print( 'Error: %s' % e)
	for x in celeryarray:
		print("--------------------------------------------------------------------------------")
		runTayne(x)


def runflarhgunnstow(tayne):
	print("Doin' a json at '"+jsonname+"'")
	try:
		results = api.search(tayne)
		print('Results found: %s' % results['total'])
		for result in results['matches']:
			celeryarray.append((result['ip_str'].encode('utf-8')))
	except shodan.APIError, e:
		print( 'Error: %s' % e)
	for x in celeryarray:
		runNudeTayne(x)

#---------------------------Funcs end here-





#---------------------------Menu junk/main starts here-
parsyboi = argparse.ArgumentParser()
parsyboi.add_argument('-s','--single_ip', help='Get details for a single IP', required=False)
parsyboi.add_argument('-q','--query_regular', help='Run a plaintext search, wrapped in quotes for multiple values, "whatever port=8080"', required=False)
parsyboi.add_argument('-c','--celery_man', help='Computer, load up celery man please. (recursive query regular)', required=False)
parsyboi.add_argument('-f','--flarh_gunn_stow', help='Show me nude tayne. (recursive query regular with json output)', required=False)
argyboi = parsyboi.parse_args()

hostsearch = argyboi.single_ip
if hostsearch >= 7:
	runTayne(hostsearch)

fullquery = argyboi.query_regular
if fullquery >= 3:
	runFullQuery(fullquery)

celeryquery = argyboi.celery_man
if celeryquery >= 1:
        runCeleryMan(celeryquery)

flarh = argyboi.flarh_gunn_stow
if flarh >= 1:
	runflarhgunnstow(flarh)

#------------------------------------closing out the json-
jason.close()
