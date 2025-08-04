def outer():
    print("Inside outer function")

    def inner():
        print("Inner Function")

    inner()

outer()

#How to invoke inner function from outside : using return 

def outer():
    def m1():
        print("m1 Function")
    def inner():
        print("Inner Function")
    return inner
value = outer()
value()