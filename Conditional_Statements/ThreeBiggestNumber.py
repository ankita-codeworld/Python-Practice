#Write a program to find the biggest of given 3 numbers from the command prompt?

n1 = int(input("Enter the first numbers:"))
n2 = int(input("Enter the second number:"))
n3 = int(input("Enter the third number:"))

if n1>n2 and n1>n3:
               print("Biggest number is:",n1)
elif n2>n3:
            print("Biggest number is:",n2)
else:
        print("Biggest number is:",n3)
