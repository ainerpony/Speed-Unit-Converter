from decimal import Decimal

print("\n","*"*14,"\n"" 1.km/h to m/s\n"" 2.m/s to km/h\n","*"*14,"\n")

i = None
s = None

while not i:
    i = input(" Select: ")

if i == str("1"):
    while not s:
        s = input(" Speed : ")
    if str.isdigit(s) or str.isdigit(s.replace(".","0")) == True:
        o = float(s)*10/36
        print("\n"" About: "+str(int(o))+"m/s")
        e = Decimal(o).quantize(Decimal("0.01"))
        print(" Exact: "+str(e)+"m/s")
    else:
        print("\n""Check your input!")

elif i == str("2"):
    while not s:
        s = input(" Speed : ")
    if str.isdigit(s) or str.isdigit(s.replace(".","")) == True:
        o = float(s)*3.6
        print("\n"" About: "+str(int(o))+"km/h")
        e = Decimal(o).quantize(Decimal("0.01"))
        print(" Exact: "+str(e)+"km/h")
    else:
        print("\n""Chack your input!")

else:
    print("Check your input!")
