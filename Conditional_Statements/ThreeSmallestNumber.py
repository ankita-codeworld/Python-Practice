#Write a program to find the Smallest of given 3 numbers from the command prompt?

n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
n3 = int(input("Enter the third number:"))
if n1<n2 and n1<n3:
    print("Smallest number is:",n1)
elif n2<n3:
    print("Smalles number is:", n2)
else:
    print("Smallest number is:", n3)