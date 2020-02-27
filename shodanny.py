#!/usr/bin/python
import shodan
import argparse
import sys, os, time

api = shodan.Shodan("ThAt-api-kEy-tho")
celeryarray = []

#---------------------------Funcs start here-

def runSingleIP(hostsearch):
        singlehost = api.host(hostsearch)
        print("""
IP: {}
Organization: {}
Operating System: {}
""".format(singlehost['ip_str'], singlehost.get('org', 'n/a'), singlehost.get('os', 'n/a')))
        for item in singlehost['data']:
                print("""
Port: {}
Banner: {}
""".format(item['port'], item['data']))



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
        time.sleep(2)


def runCeleryMan(tayne):
        try:
                results = api.search(tayne)
                print('Results found: %s' % results['total'])
                for result in results['matches']:
                        celeryarray.append((result['ip_str'].encode('utf-8')))
        except shodan.APIError, e:
                print( 'Error: %s' % e)
        for x in celeryarray:
                print("-------------------------╭∩╮(Ο_Ο)╭∩╮-------------------------")
                runTayne(x)


def flarhgunnstow():
        #build a workable json here
        print("meow")

#---------------------------Funcs end here-


#---------------------------Menu junk/main starts here-
parsyboi = argparse.ArgumentParser()
parsyboi.add_argument('-s','--single_ip', help='Get details for a single IP', required=False)
parsyboi.add_argument('-q','--query_regular', help='Run a plaintext search, wrapped in quotes for multiple values, "whatever port=8080"', required=False)
parsyboi.add_argument('-c','--celery_man', help='Computer, load up celery man please. (recursive query regular)', required=False)
parsyboi.add_argument('-f','--flarh_gunn_stow', help='Build a fun and nice json to do super legal things with! (recursive query regular with json output)', required=False)
argyboi = parsyboi.parse_args()

hostsearch = argyboi.single_ip
if hostsearch >= 7:
        runSingleIP(hostsearch)

fullquery = argyboi.query_regular
if fullquery >= 3:
        runFullQuery(fullquery)

celeryquery = argyboi.celery_man
if celeryquery >= 3:
        runCeleryMan(celeryquery)

flarh = argyboi.flarh_gunn_stow
if flarh >= 3:
        runflarhgunnstow(flarh)
