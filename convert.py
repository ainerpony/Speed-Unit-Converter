import time
from decimal import Decimal

print("\n","*"*14,"\n"" 1.km/h to m/s\n"" 2.m/s to km/h\n","*"*14,"\n")
error = "No option"

while True:
    i = input("Select: ")
    if str.isdigit(i):
        break
    else:
        print("Enter number only")
if i == str(1) or i == str(2):
    while True:
        s = input("Speed: ")
        if str.isdigit(s) or str.isdigit(s.replace(".","")):
            if s.count(".") < 2:
                break
            else:
                print("Enter number or float")
        else:
            print("Enter number only")

if i == str(1):
    o = float(s)*10/36
elif i == str(2):
    o = float(s)*3.6

if i == str(1) or i == str(2):
    e = Decimal(o).quantize(Decimal("0.01"))
    print("\n""About: ",int(o),"m/s")
    print("Exact: ",e,"m/s")
else:
    print("\n",error,"\n")
