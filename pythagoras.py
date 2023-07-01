from math import sqrt

print("a is opposite, b is adjacent and c is hypothenus ")
fo = input("Which sides a,b,c to be calculated? : ")
if fo == "c":
    sa = int(input("Enter side a: "))
    sb = int(input("Enter side b: "))
    sc = sqrt(sa * sa + sb * sb)
    print("The length of side c is: ", sc)
elif fo == "a":
    sb = int(input("Enter side b: "))
    sc = int(input("Enter side c: "))
    sa = sqrt(sc * sc - sb * sb)
    print("The length of side a is: ", sa)
elif fo == "b":
    sa = int(input("Enter side a: "))
    sc = int(input("Enter side c: "))
    sb = sqrt(sa * sa - sc * sc)
    print("The length of side b is: ", sb)

else:
    print("Please select the correct side between a,b,c.")