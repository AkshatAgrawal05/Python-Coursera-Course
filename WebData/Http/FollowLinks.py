# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

def followLink(url,position):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    for i in range(0, len(tags)):
        # print(tag.get('href', None))
        tag = tags[i]
        link = tag.get('href', None)
        if(i == position-1):
            print(link)
            return link

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = input('Enter Count - ')
position = input('Enter position - ')

for c in range(0,int(count)):
    url = followLink(url,int(position))
