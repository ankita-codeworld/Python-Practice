def addplus(mark):
    return mark+1

marks = [35,36,37,38]
map_obj = map(addplus,marks)

new_marks = list(map_obj)
print(marks)
print(new_marks)