fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)

count = 0
for line in fh:
    line = line.rstrip()
    if "From " in line:
        count = count + 1
        spltLst = line.split()
        print(spltLst[1])

print("There were "+str(count)+" lines in the file with From as the first word")
