import re

fileName = input('Enter fileName: ')

try:
    fhandle = open(fileName)
except Exception as e:
    print('Invalid FileName')
    quit()

numList = list()
for line in fhandle:
    line = line.rstrip()
    lineList = re.findall('[0-9]+',line)
    numList = numList + lineList

sum = 0;
for num in numList:
    sum = sum + int(num)

print(sum)
