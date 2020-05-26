def computepay(h,r):
    if(h > 40):
        reg = h * r
        otp = (h - 40) * (r * 0.5)
        return reg + otp
    else:
        return h * r


hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate: ")
r = float(rate)
p = computepay(h,r)
print("Pay",p)
