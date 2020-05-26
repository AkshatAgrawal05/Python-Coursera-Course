# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except Exception as e:
    print("Invalid File Name")
    quit()

count = 0
add = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(" ");
    slice = line[pos+1:]
    add = add + float(slice)
    count = count + 1

average = add/count
print("Average spam confidence:", average)
