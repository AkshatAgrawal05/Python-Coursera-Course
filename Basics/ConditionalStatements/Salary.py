hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)

if(h > 40):
    reg = h * r
    otp = (h - 40) * (r * 0.5)

    pay = reg + otp

else:
    pay = h * r

print(pay)
