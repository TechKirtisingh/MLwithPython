### ^^^^^^^^ If Else Loops ^^^^^^
"""a=int(input("Enter your age: "))
print("your age is:",a)
# Conditional Operators::-->>
# >,<,>=,<=,==,!=
# print(a>18)
# print(a<18)
# print(a>=18)
# print(a<=18)
# print(a==18)
# print(a!=18)


if(a>18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")"""
 
    
"""
applePrice = 10 
budget =200
if(budget-applePrice >= 50):
    print("You can buy apples")
else:
    print("You cannot buy apples")
"""


""" elif....
    
num = int(input("Enter the value of num:"))
if(num<0):
    print("Number is negative")
elif(num==0):
    print("number is zero")
elif(num==99):
    print("Number is Special")
else:
    print("number is positive")
    
print("i am happy")    """  

    

""" 
num=18
if(num<0):
    print("Number is negative")  
elif(num>0):
    if(num%2==0):
        print("Number is positive and even")
    elif(num%2!=0):
        print("Number is positive and odd")
    else:
        print("Number is not even or odd") 
else:
    print("Number is zero")     
    """            
    
 
 # match case  (act as a switch case)

 
"""
x=2
match x:
     case 1:
         print("x is 1")
     case 2 if x% 2 == 0:  # additional condition
         print("x is 2 and even")
     case 3 if x <10:  # additional condition
         print("x is 3 and less than 10")
     case _:
         print("x is something else")  # default case  
""" 
 
 ###   for loops...
 
 
"""   
password = "hey there is something in this new happen after a long time"
for i in password:  
    print(i)
    if(i=="f"):
        print("found f")
"""


"""   
colors = ["red", "green", "blue", "yellow","purple"]
for color in colors:
    print(color)
    if(color== "yellow"):
        print("Found yellow")
            
    for i in color:
        print(i)
"""

##table.....

"""
n=int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)                         
    
 """         


# for loop with range (start, stop, step)
#stop: n-1 

"""
for k in range(5):
    print(k+1)
for p in range(1, 10):  # start, stop  
    print(p, end=" ")  # end parameter to avoid new line after each print
for q in range(1, 10, 2):  # start, stop, step
    print(q)
for r in range(10, 0, -1):  # start, stop, step (decrementing)
    print(r)
"""  
    
# while loops.....
"""
i=0
while(i<3):
    print(i)
    i=i+1
print("done with the loop")        
 """ 
 
"""   
i=int(input("Enter a number: "))  
while (i<=30):  
 i=int(input("write number: "))  
 print(i)  
 """   
    
"""
n=5
while (n > 0):
    print("Countdown:", n)
    n = n-1; 
print("happy birthday")  
"""
   
# break means loop ko chodo aur bahar aa jao
#continue means loop ko skip karo aur next iteration pe jao
   
"""
for i in range(12):
    if (i==10):
        break 
    print("5 X", i, "=" , 5*i)
print("out of the loop")
      
"""

"""
for m in range(12):
    if (m==10):
        print("skip the loop")
        continue 
    print("6 X", m, "=" , 6*m)
  """
  

"""
i=0
while True:
    print(i)
    i= i+1
    if(i%20==0):
         break
"""

