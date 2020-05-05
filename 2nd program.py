#program to accept 'n' number from user and calculate sum of all number between 1 and n including n
n = input("Enter number to calculate sum")
n = int(n)
sum = 0
for num in range (0, n+1, 1):
    sum = sum+num
print("Sum of the first",n,"numbers is-",sum)    
