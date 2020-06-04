import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url - ')
str = urllib.request.urlopen(url).read()
commentInfo = ET.fromstring(str)
lst = commentInfo.findall('comments/comment')
print('Count: ',len(lst))
sum = 0
for item in lst:
    # print('count : ',item.find('count').text)
    count = int(item.find('count').text)
    sum = sum + count

print('Sum: ',sum)
