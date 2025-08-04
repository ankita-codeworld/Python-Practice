# List

l1 = [10,20,30,40]
#index 0, 1, 2, 3
l1[2] = 44  # In list we can update or change
print(l1)


# Tuple 

t1 = (10,20,30,40)
#index 0, 1, 2, 3
t1[1] = 33    # It will give us error. It will give Type error
print(t1)

#Set

s1 = {10,20,30,40}
s1.add(50)  
print(s1)    # In Set we can change or update


#Bytes

b = bytes([10,20,30,40])
#index     0, 1, 2, 3
b[2] = 33        # It will give us error. It will give Type error
print(b)


#ByteArray

ba = bytearray([10,20,30,40])
#index          0, 1, 2, 3
ba[2] = 33
print(ba)

