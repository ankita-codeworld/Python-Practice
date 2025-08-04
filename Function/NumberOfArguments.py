'''def my_func(fname):
    print(fname + " Hello ")
my_func("Hi")'''



# 2 Arguments

'''def my_func(fname,lname):
    print(fname + " " + lname)
my_func("Hi", "Hello")'''

# If we do not know how many arguments we need to pass use *

def my_fun(*subject):
    print("This is not comes under" + subject[2])

my_fun("Hindi","English", " Maths ")

'''def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")'''