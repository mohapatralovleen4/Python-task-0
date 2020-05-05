#program to accept 2 integer numbers and return their product and if the product is greater then 1000 then return its sum

a = int(input("Enter first integer\n"))
b = int(input("Enter second integer\n"))
c = a*b
if c>1000:
    print (a+b)
else:
    print (c)
