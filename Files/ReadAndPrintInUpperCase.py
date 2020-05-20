fname = input("Enter file name: ")
try:
    fh = open(fname)
except Exception as e:
    print("Invalid File Name")
    quit()

for line in fh:
    line = line.rstrip()
    line = line.upper()
    print(line)
