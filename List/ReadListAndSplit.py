fname = input("Enter file name: ")
try:
    fh = open(fname)
except Exception as e:
    print("Invalid File Name")
    quit()

lst = list()
for line in fh:
    line = line.rstrip()
    spltLst = line.split()
    for word in spltLst:
        if word not in lst : lst.append(word)

lst.sort()
print(lst)
