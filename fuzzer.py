import sys, requests, os, argparse, json
os.system('clear')
##################################
parse = argparse.ArgumentParser()
parse.add_argument("url")
arguments = parse.parse_args()
##################################
def fuzz(url, word):
    r = requests.get(url+word+'/')
    if str(r.status_code) == '404':
          print('Failed url '+url+word+'/')
    if str(r.status_code) == '403':
          print('Found but cannot access '+url+word+'/')
    if str(r.status_code) == '200':
          print('Found url '+url+word+'/')

fuzzlist = json.loads(open('fuzzlist.json').read())
for dirs in fuzzlist:
    fuzz(arguments.url, dirs)

