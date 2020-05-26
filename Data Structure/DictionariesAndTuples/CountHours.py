"""
Write a program to read through the mbox-short.txt and figure out the distribution by
 hour of the day for each of the messages. You can pull the hour out from the 'From ' line
  by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour
 as shown below.
"""
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hour = dict()

for line in handle:
    line = line.rstrip()
    if "From " in line:
        splLine = line.split()
        time = splLine[5]
        timeSplt = time.split(':');
        hrs = timeSplt[0]
        hour[hrs] = hour.get(hrs,0) + 1

hourList = list(hour.items())
hourList.sort()

for k,v in hourList:
    print(k,v)
