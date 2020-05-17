largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break

    try:
        inum = int(num)
        if largest is None or largest < inum:
            largest = inum
        elif smallest is None or smallest > inum:
            smallest = inum

    except Exception as e:
        print("Invalid input")
        continue


print("Maximum is ",largest)
print("Minimum is ",smallest)
