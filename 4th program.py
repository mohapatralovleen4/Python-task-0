#program to input a string and display only those characters which are present at an even index number

str =input("Enter a string\n")
index = 0
while (index<len(str)):
    print(str[index],end='')
    index = index + 2
