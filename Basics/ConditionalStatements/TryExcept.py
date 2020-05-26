astr = "Hello Bob"
try:
    istr = int(astr)
except:
    istr = -1

print("First",istr)

astr = "123"
try:
    istr = int(astr)
except Exception as e:
    istr = -1

print("Second",istr) 
