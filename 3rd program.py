#program to count the total number of digits in a given number

n = int(input("Enter a number to calculate the number of digits\n"))
c = 0
while(n>0):
   c = (c+1)
   n = (n//10)
print("The number of digits in the given number are",c)   
