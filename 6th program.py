#program to print fibonacci series and to check if a number is fibonacci or not

nterms = int(input("Enter numbers of terms to generate fibonacci sequence"))
n1,n2 = 0,1
c = 0
if(nterms<=0):
    print("Enter a positive integer")
elif(nterms==1):
    print("Fibonacci sequence upto",nterms,"is- ")
    print(n1)
else:
    print("Fibonacci sequence:")
    while(c<nterms):
        print(n1)
        n = n1+n2
        n1 = n2
        n2 = n
        c = c+1

#to check if a number is fibonacci number or not 


import math

def CheckPerfectSquare(x):
    sqrt = int(math.sqrt(x))
    if pow(sqrt,2) ==x:
        return True
    else:
        return False

def isFiboNumber(x):
    res1= 5*x*x + 4
    res2= 5*x*x - 4
    if( CheckPerfectSquare(res1) or CheckPerfectSquare(res2)):
        return True
    else:
        return False
num = int(input("Enter an integer to check if a number is fibonacci or not\n"))
if(isFiboNumber(num)):
    print("Yes")
else:
    print("No")

    
    
    
