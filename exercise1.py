# create calculator::--->>>
"""a= int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("sum os a and b is",a+b)
print("difference of a and b is",a-b)    
print("product of a and b is",a*b)
print("division of a and b is",a/b)
print("modulus of a and b is",a%b)
print("exponential of a and b is",a**b)"""


"""time=int(input("Enter time in hour: "))
if(time>=0 and time<12):
    print("Good Morning")
elif(time==12):
    print("Good Noon")
elif(time>12 and time<17):
    print("Good Afternoon")
elif(time>=17 and time<20):
    print("Good Evening")   
else:
    print("Good Night")  """
    
 
 # /////////// time module  //////////// 
    ## strftime() method:it is a function that returns the current time in the specified format.
    
"""    
import time
current_time = time.strftime("%H:%M:%S")
print("Current Time:", current_time)  
current_time = time.strftime("%H")
print("Current Hour:", current_time) 
current_time = time.strftime("%M")
print("Current Minute:", current_time)      
current_time = time.strftime("%S")
print("Current Second:", current_time)
if(int(current_time) >= 0 and int(current_time) < 12):
    print("Good Morning")
elif(int(current_time) == 12):
    print("Good Noon")      
elif(int(current_time) > 12 and int(current_time) < 17):
    print("Good Afternoon")
elif(int(current_time) >= 17 and int(current_time) < 20):
    print("Good Evening")
else:
    print("Good Night")      
              
"""


         
               