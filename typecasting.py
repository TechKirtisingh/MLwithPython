"""x ="10"
y ="2"
print(x+y) # This will concatenate the strings "10" and "2", resulting in "102"
print(int(x)+int(y)) # This is explicit type casting

w=1.9
z=3
print(w+z) # This will add the float 1.9 and the integer 3, resulting in 4.9"""



"""String Slicing and Operations on String"""

"""names = "kirti , nihal , ayush , khushi"
#inculding 0 but not including 5
#so it will include characters from index 0 to index 4 
print("length of names is \n", names[0:5] ,"\n", len(names))
#names[0:5] will print the first 5 characters of the string
#len(names) will print the length of the string 
print(names[:]) # will print the entire string

print(names[:5])# automatically added 0 at the start

print(names[7:]) # will print the string from index 7 to the end

print(names[0:-12])# will print the string from index 0 to the index -12 (which is the 12th character from the end)

print(names[-1:4])# will print an empty string because -1 is the last character and 4 is the 5th character from the start, so there is no character between them

print(names[-7:-1])#will print the string from index -7 to the index -1 (which is the last character)"""


""" important.......

nm="harry"
print(nm[-4:-2])#[(5-4 :: 5-2)=> -4 to -2] will print the characters from index -4 to index -2 (which is the 2nd character from the end)  """

# $$$ String Methods $$$ 
#Strings are immutable, meaning they cannot be changed after creation.
#string makes new string with changes applied in existing string.

a=" hey @@@ RadheKrishna @@@@@@"


"""print(a.upper()) 
print(a.lower())
print(a.rstrip("@")) # removes the @ from the end of the string
print(a.lstrip("@")) # removes the @ from the start of the string
print(a.replace("@", "shree"))
print(a.split(" ")) # splits the string into a list 
print(a.capitalize())"""


str1 = "Welcomeee to Python Programming Language and its basics"


"""
print(len(str1))# Length of the string

print(len(str1.center(50)))# Center the string within 50 characters using space...

print(a.count("@"))

print(a.endswith("@@@"))#check wheather it is end with @ or not

print(a.endswith("Ra",6,10))##check wheather it is end with Ra or not from index 6 to 10

print(a.startswith("hey"))#check wheather it is start with hey or not

print(a.find("Radhe"))#find the index of the first occurrence of "Radhe" in the string

print(str1.index("to"))#find the index of the first occurrence"""

"""

str2=" Welcometotheconsole"
print(str2.isalnum())#check if the string is alphanumeric (contains only letters and numbers)

print(str2.isalpha())#check if the string is alphabatic (contains letter)

print(str2.isprintable())#check if the string is printable(if it contain \n or \t then it is not printable)

b=" "
print(b.isspace())#check if the string contains only whitespace characters

print(str2.istitle())#check if the string is in title case (first letter of each word is capitalized)

str3="HelloWorld"
print(str3.swapcase())#swap the case of each character in the string (uppercase to lowercase and vice versa)

D="His name is Ayush. ayush is a good programmer."
print(D.title())#convert the first letter of each word to uppercase and the rest to lowercase
 
"""


