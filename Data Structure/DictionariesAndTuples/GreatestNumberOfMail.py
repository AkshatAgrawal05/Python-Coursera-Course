"""
Write a program to read through the mbox-short.txt and figure out who has sent the greatest
number of mail messages. The program looks for 'From ' lines and takes the second word of
those lines as the person who sent the mail. The program creates a Python dictionary that
maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a
maximum loop to find the most prolific committer.
"""
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
nameCount = dict()
for line in handle:
    line = line.rstrip()
    if "From " in line:
        splLine = line.split()
        name = splLine[1]
        nameCount[name] = nameCount.get(name,0) + 1

bigword = None
bigCount = None
for key,value in nameCount.items():
    if bigCount is None or bigCount < value:
        bigword = key
        bigCount = value

print(bigword,bigCount)
