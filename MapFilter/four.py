enames = ['rahul', 'sonia','amir']
def changecase(ename):
    return ename.upper()

new_enames= list(map(changecase,enames))
print(new_enames)