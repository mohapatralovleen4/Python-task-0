#program to print all the prime numbers in a given interval and to also check the input number is prime or not

lower = int(input("Enter the lower range\n"))
upper = int(input("Enter the upper range\n"))

for num in range(lower,upper+1):
   if(num>1):
     for i in range(2,num):
            if((num%i)==0):
                 break
            else:
                print(num)

#how to check a number is prime or not
a = int(input("Enter a number to check if its prime or not"))
j=1
if(a>1):
    for j in range(2,a):
        if((a%j)==0):
            print(a,"is not a prime number")
            break
        else:
            print(a,"is a prime number")
else:
    print(a, "is not a prime number")
    
            
