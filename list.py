###      LIST METHODS      ###

"""
lst_exmp = []
print (type(lst_exmp)) # empty list

lst=["maths", "science", 100,200,300]
print(type(lst))
print(len(lst)) # length of the list
print(lst*2) # it will repeat the list 2 times
"""

# APPEND METHOD
"""lst.append("english") # adds "english" to the end of the list
print(lst)
lst.append(["history", "geography"]) # it create a nested list
print(lst)       """

# INDEXING IN LIST
"""print(lst[0]) # prints the first element of the list
print(lst[4])
print(lst[2:5])
print(lst[2:])     """

## INSERT METHOD
"""lst.insert(2, "Kirti") # inserts "computer" at index 2
print(lst)      """

## EXTEND METHOD
"""lst2 = [1,2,3,2,4,6,2,7,2]
lst2.extend([5,8,9]) # here we add elements without creating a nested list
print(lst2)"""

# Various operation that can be performed on list
"""sum(lst2) # sum of all elements in the list
print(sum(lst2))

   
    #1.    POP METHOD
lst2.pop(1) # removes the second element (index 1) from the list
print(lst2)
   #2.    COUNT METHOD
print(lst2.count(2)) # counts the number of occurrences of 2 in the list
   #3.    INDEX METHOD  
print(lst2.index(1,0,4)) # returns the index of the first occurrence of 1 in the list from index 0 to 4
   #4.   MIN AND MAX METHOD
print(min(lst2)) # returns the minimum value in the list
print(max(lst2)) # returns the maximum value in the list
"""
 
 
 ####    SETS  (does not supprting indexing)  ####

"""
set_var = set() # creates an empty set
print(type(set_var)) # <class 'set'>

set_var = {"Avengers" , "Ironman", "Hitman" , "Spiderman"} # creates a set with elements from 1 to 10
print(set_var)
print(type(set_var))

set_var1= {1,2,3,4,1,2,4,56,7,6}
print(set_var1) # sets do not allow duplicate elements, so it will remove the duplicates """


# INBUIT FUNCTIONS IN SETS
"""
set_var.add("Thor") # adds "Thor" to the set
print(set_var)

set1 = {"Spiderman","Thor","Ironman"}
set2 = {"Hitman","Rocket","Spiderman","Thor"}
print(set2.difference(set1))
print(set2.difference_update(set1))


set3 = {"Spiderman","Thor","Ironman"}
set4 = {"Hitman","Rocket","Spiderman","Thor"}
print(set3.intersection(set4))
print(set3.intersection_update(set4)) 
"""

####  ******* DICTIONARY ****** ####

"""
dic = {}
print(type(dic)) # creating a empty dictionary (only use key:value pair)

my_dic ={"Car1": "Audi" ,"Car2":"BMW","Car3":"Mercidies Benz" }
print(type(my_dic))
print(my_dic['Car2']) # Access the item value based on keys"""

#        forloop

# print of only key
"""for x in my_dic:
   print(x)"""

# print of only values
"""for x in my_dic.values():
   print(x)"""

#check of both key & value 
"""for x in my_dic.items():
   print(x) """

# Adding item in the dictionaries::
"""my_dic["car4"] = "Audi 2.0" 
print(my_dic)

my_dic.update({"car5":"Volkswagen Polo"})
print(my_dic)"""

# whenever we append value its overwritte on each other
"""my_dic ['Car1'] = "MAruti"
print(my_dic)"""


#  $$$$   NESTED DICTIONARY    $$$$

"""car1_model = {'Mercendes':1960}
car2_model = {'Audi':1970}
car3_model = {'Ambassador':1980}

car_type={'car1':car1_model, 'car2':car2_model, 'car3':car3_model}
print(car_type)"""

# Accessing the items in the dictionary
"""
print(car_type['car1'])

print(car_type['car2']['Audi'])"""


####  ^^^^^^  TUPLES  ^^^^   ######

# Create an empty Tuples

my_tuple = tuple()
print(type(my_tuple))

mytup = ("krish","Ankur","John")
print(mytup)
print(mytup[0]) # indexing.... 


# tuple object does not support item assignment
# mytup[0]='Naik'
# print(mytup)

## it can replce whole tuple ::::(not one of them)


#  INBUILT FUNCTION

print(mytup.count('krish'))

print(mytup.index('Ankur'))

