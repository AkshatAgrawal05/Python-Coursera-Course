import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
data = urllib.request.urlopen(url).read().decode()

js = json.loads(data)

print(json.dumps(js, indent=4))

comments = js['comments']

sum = 0
for comment in comments:
    count = comment['count']
    sum = sum + count

print('Sum: ',sum)
