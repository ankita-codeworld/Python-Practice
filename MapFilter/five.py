# To collect Even numbers from given set of list.

numbers = [44,78,17,19,82,7]

def even_no(num):
    return num%2 == 0
even_numbers = list(filter(even_numbers, numbers))
print(even_numbers)