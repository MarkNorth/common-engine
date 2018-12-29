import sys, requests, os, argparse, json, random, string
sys.tracebacklimit = 0
os.system('clear')
##################################
parse = argparse.ArgumentParser()
parse.add_argument("url")
arguments = parse.parse_args()
##################################
count = 0
def fuzz(url, word):
    global count
    r = requests.get(url+word+'/')
    #if str(r.status_code) == '404':
         # print('Failed url '+url+word+'/')
    if str(r.status_code) == '403':
          print('Found but cannot access '+url+word+'/')
          count = count + 1
    if str(r.status_code) == '200':
          print('Found url '+url+word+'/')
          count = count + 1
    if str(r.status_code) == '302':
          print('Found url '+url+word+'/')
          count = count + 1
##################################
def randomDir(size=6, chars=string.ascii_lowercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))
fuzzlist = json.loads(open('fuzzlist.json').read())
for dirs in fuzzlist:
       fuzz(arguments.url, dirs)
print('Finished and found: ' + str(count) + ' URLs.')
