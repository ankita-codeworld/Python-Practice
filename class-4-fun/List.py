#List : Group of elements as one entity. It allowed duplicates and hrtrogenous elements.
        # Stroring based on indexing. negative index is also possible.
        # Insertion order maintained.
        # we can iterate list of object using 

# Create
l1 = [] # Empty list
l2 = [10,20,30]
l3 = [10,20.5,"Rahul",10,"Rahul",True]

#Read
print(l1)    #[]
print(l2)    #[10,20,30]

# How to read list elements (using indexing)

numbers = [10,20,30,40]
#index      0, 1, 2, 3
print(numbers[0])
print(numbers[1])
print(numbers[3])


#Create a list and read list of elements using indexing

numbers = [10,20,23,40]
print(numbers[0])
print(numbers[1])
#print(numbers[5])  # it will give us index error because index value is not 5 here.

#Update & Delete

numbers[2] = 33    #update
print(numbers)


del numbers[1] 
