#Positional Argument

def sub(a,b):
    print(a - b)

sub(100,200)        #100
sub(200,100)        # -100

#keyword Argument

def sub(a,b):   
    p(a,b)

sub(100,200)    #100
sub(200,100)    #100

# Default Argument
def add(a,b,c):
    print(a+b+c)

add(10,20,30)       #60
add(10,20)          #Error we'll get because 1 argument is missing

# var length Argument

def add(a,*b):
    print(a,"_",b)
    
add(10,20)
add(10,20,30)
add(10,20,30,40)