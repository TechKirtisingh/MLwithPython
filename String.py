## string concept............
"""
def str(name):
    return"Hello {} , welcome to the community".format(name) # .formate () is used to insert the value of name in the string.
print(str("Kirti"))

def str(firstname,secondname):
    return"Hello {name} , welcome to the community Mr {lsname}".format(name=firstname, lsname=secondname) 
print(str("Kirti","Singh"))

"""

### PYTHON LIST ITERABLE VS ITERATORS..........

lst=[1,2,3,45,6,7]
for i in lst:
    print(i)  # This is an iterable, it can be iterated over directly.
lst1=iter(lst)  # This creates an iterator object from the list.
print(lst1)  # Output: <list_iterator object at 0x...>

# property of iterator is  when you create an iterator, it does not store all the values in memory, it just stores the current value and the next value.   whereas  in iteration values are not all the value stored in the memory   or it is not initialized in the memory location but when you called a fucntion next() then the value will get stored or initialized in the memory location. 


# one by one value will be stored in the memory location and it will be initialized in the memory location when you call the next() function.
print(next(lst1))  # Output: 1
print(next(lst1))  # Output: 2  
for i in lst1:
    print("the value is:",i)























































































































































































