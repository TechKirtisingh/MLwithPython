"""
def calculate_simplifiication(a,b):
   mean = (a + b) / (a-b)
   print(mean)

def isgreater(a, b):
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")  
        
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    print("Area of circle is:", area)
    
def rectangle_area(a, b):
    area = a* b
    print("Area of rectangle is:", area) 
    
def islesser(a,b):
    pass                     
        
a = 8
b = 2
# if(a>b):
#     print("a is greater than b")
# else:
#     print("b is greater than a")
isgreater(a, b)       
calculate_simplifiication(a, b)
area_of_circle(5)
rectangle_area(a, b)

#calculate_simplifiication = (a + b) / (a - b)
#print(calculate_simplifiication)

c=12
d=24
# if(c>d):
#     print("c is greater than d") 
# else:
#     print("d is greater than c")   
isgreater(c, d)                
calculate_simplifiication(c, d)
area_of_circle(10)
rectangle_area(c, d)
islesser(c, d)
#calculate_simplifiication = (c + d) / (c - d)
#print(calculate_simplifiication)
   
 """   
 # Function Arguments..............
 

"""def average(a, b=4 ,c=1):
    print("The average is: ", (a + b + c) / 2)

#default argument::
average(4,5,6)
average(1)
         
#keyword argument:: (order change)    
average(c=3, a=3, b=2)    
    
#required argument:: 
average(a=2)
"""
"""
#variable-length argument::   
def avg(*num): 
    print(type(num))  # tuple
    sum=0
    for i in num:
        sum= sum+i
        print("The average is:", sum / len(num))
avg(5,6)        
  """  

"""
def name(fname,mname="Rajput",lname="Singh"):
    print("My name is", fname, mname, lname)
name("kirti","Singh","Rajput")
name("khushi")    
 """  
 
 ### print vs return............
""" 
def  add(a, b):
    return a + b
addition = add(5,6)
print("The addition is:", addition)
 """
 
"""
def hello(name , age=30):
    print("My name  is {} and my age is {}".format(name, age))## .formate: ka kam hota hai ki string ke andar jo bhi {} hai usme value pass kar deta hai
hello("kittu",26)
# hello() # type error: hello() missing positional argument: 'name'

 
 
def hello(*arg,**kwargs):
    print("Positional arguments:", arg)
    print("Keyword arguments:", kwargs)
hello('kittu', 'khushi', age=26, dob=1990)  # *arg: tuple, **kwargs: dictionary
list = ['kittu', 'khushi'] 
dict_arg = {'age': 26, 'dob': 1990}
hello(list, dict_arg)  # Passing list and dictionary as single arguments (taking them as single arguments which is not the intended use)
hello(*list, **dict_arg)  # Unpacking the list and dictionary  
 """
# Function to calculate the sum of even and odd numbers in a list
""" 
lst= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
def evenoddsum(lst):
    even_sum = 0
    odd_sum = 0
    for i in lst:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return even_sum, odd_sum 
print(evenoddsum(lst)) 
 """
 ## Lambda Functions........
    # Lambda functions are also called  anonymous functions defined using the `lambda` keyword. They can take any number of arguments but can only have one expression. They are often used for short, throwaway functions.
""" 
def add(x, y):
    return x + y
print(add(4,5) )
 #////     OR      ////////
addition=lambda a,b: a + b 
print(addition(12,14) )
 """
 
 #  EVEN FUNCTION..........
""" 
def even(num):
    if num%2==0:
        return True
    else:
        return False 
print(even(10))    
#  ////  or    ////
even = lambda a:a%2==0
print(even(10))  # Output: True
""" 
"""
def addi(x,y,z):
    return x + y + z
print(addi(1,2,3)) 
#////   or   ////
add= lambda a,b,c: a + b + c
print(add(5,4,6))
"""

#//////////////////////   MAP FUNCTION..............
"""
def square(x):
    return x * x
print(square(5))

lst=[2,5,3,4,78,12,13,25,15]
print(list(map(square, lst)))  # Using map to apply the square function to each element in the list
"""

#//////////// FILTER  #############
## filter function is used to filter elements from an iterable based on a function that returns True or False for each element.
"""
def even(num):
    if num%2==0:
        return "Even"
lsst = [1,4,5,7,8,0,4,5,12,13] 
filter(even,lsst)# bina list ke ye output return nii karta hai, isliye list me convert karna padta hai
print(list(filter(even,lsst)) )

#////  or  ////

print(list(filter(lambda x: x % 2 == 0, lsst)) ) # Using filter with a lambda function to get even numbers

print(list(map(lambda x: x % 2 == 0, lsst)) )
"""

##    list comprehension..
#    list comprehension provides a concise way to create lists based on existing lists or other iterables. It consists of brackets containing an expression followed by a `for` clause, and can also include optional `if` clauses.The expression can be anything meaning you can put in all kinds of objects in lists.

"""
lst1=[]
def lst_sq(lst):
    for i in lst:
        lst1.append(i*i) ## apend function use krke list me value add krte hai
    return lst1
lst_sq([1,2,3,4,5])
print(lst1)


lst=[[1,2,3,4,5,6,7]]
#%%% convert to list comprehension %%%

# lst2 = [i*i for i in lst if i%2==0] ## is true but can't support in this...
#print(lst2) # output : [4,16,36]

"""






 
 