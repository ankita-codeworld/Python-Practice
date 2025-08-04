ba = bytearray([10,20,30,40])
#index          0, 1, 3, 4

ba[2] = 33
print(ba)    #Output : bytearray(b'\n\x14!(')

for element in ba:
    print(element)