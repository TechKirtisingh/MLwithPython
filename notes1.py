''' $$$$$ What is Python?


# $$$$$ Features of Python

# Python is simple and easy to understand.
# It is Interpreted and platform-independent which makes debugging very easy.
# Python is an open-source programming language.
# Python provides very big library support. Some of the popular libraries include NumPy, Tensorflow, Selenium, OpenCV, etc.
# It is possible to integrate other programming languages within python.

# $$$$$$ Why is Python used for

# Python is used in Data Visualization to create plots and graphical representations.
# Python helps in Data Analytics to analyze and understand raw data for insights and trends.
# It is used in AI and Machine Learning to simulate human behavior and to learn from past data without hard coding.
# It is used to create web applications.
# It can be used to handle databases.
# It is used in business and accounting to perform complex mathematical operations along with quantitative and qualitative analysis.

%%%%%% ESCAPE SEQUENCE CHARACTERS %%%%%%%%

To insert character that cannot be directly used in a string we use as an escape sequence character.
## for example \(backslash) followed by a character will insert .
print("this will\"execute")
>> sep = 'separator': specify how to separate the objects, if there is more than one objects."
>>end = 'end': specify what to print at the end of the output
>>file: An object with a write method. Default is sys.stdout
&&&& DATATYPES AND VARIABLES &&&&
    integer
    boolean
    string
    list: immutable (not changeable)
    tuple: mutuable (changeable)
    dictonary: key-value pair
    
 $$$$    Arithematic opertators $$$$
    addition: +
    subtraction: -
    multiplication: *
    division: /
    modulus: %
    exponentiation: **
    floor division: //
    
$$$$$$   Type casting $$$$$$
     the conversion of one data type to another is called type casting.
     python supports a wide varity of functions or methods like: int(), float(), str(), complex() ,hex(),dict(),set() etc. to convert one data type to another.
     
   two types of typecasting:
   1. implicit typecasting: automatic conversion of one data type to another by the interpreter.
   2. explicit typecasting: conversion of one data type to another by the programmer using type casting functions. 
   
   ***** STRING SLICING and OPERATION ON STRING *****
    %1% Length of a string :- find length of the string using len() function.
    %2% String as an array :- each character in a string can be accessed using its index. Index starts from 0.
    %3% loop through a string :- we can loop through a string using "for" loop.
^^^^ STRING METHODS ^^^^
    $ upper() : converts all characters in a string to uppercase.
    $ lower() : converts all characters in a string to lowercase.
    $ capitalize() : converts the first character of a string to uppercase and all other characters to lowercase.
    $ title() : converts the first character of each word in a string to uppercase and all other characters to lowercase.
    $ strip() : removes leading and trailing whitespace characters from a string.
    $ replace() : replaces a substring in a string with another substring.
    $ isalpha() : checks if all characters in a string are alphabetic.
    $ isalnum() : checks if all characters in a string are alphanumeric.
    $ isspace() : checks if all characters in a string are whitespace characters.
    $ islower() : checks if all characters in a string are lowercase.
    $ isupper() : checks if all characters in a string are uppercase. 
    $ isprintable() : checks if all characters in a string are printable.
    $ startswith() : checks if a string starts with a specified substring.
    $ endswith() : checks if a string ends with a specified substring.  
    $ find() : returns the index of the first occurrence of a substring in a string. If the substring is not found, it returns -1.
    $ index() : kb pahali baar aya hai wo letter ka index return karta hai, agar wo letter nahi mila to error dega. 
    $ centre() : centers a string within a specified width, it adds spaces to the left and right of the string.
    $ split() : splits a string into a list based on space.
 
### (((((((BOOLEN AND LOGICAL OPERATORS)))))) ###
   1. true and true => true
   2. true and false => false 
   3. true or true => true
   4. true or false => true 


$$$     ***** LIST *****   $$$$$
    A list is a data structure that is mutuable, ordered squence of elements.Each element or value that is inside a list is called an item.
    Lists are defined by having values between square brackets [].
  

$$$   ********  SETS  *********   $$$$$   
   A set is an unoderered collection datatype that is iterable(""), mutable, and does not allow duplicate elements. 
   based on a data structure called hash table.
   Sets are defined by having values between curly brackets {}.
   
$$$   ************     DICTIONARY  **********  $$$
   A dictionary is a collectionu which is unordered , changeable and indexed. In Python dictionaries are written

$$$$   ^^^^^^^^^^^^ Tuple ^^^^^^^^^^$$$$$$     

Tuple : ()
 
    
 #  $$$$$  conditional statement  $$$$$$ 
  if, else, elif are used to make decisions in a program.
  
##### MATCHCASE STATEMENT #####    
# Match-case statement is used to match a value against a pattern.
to implement switch case like charachteristics very similar to if-else functionality , we use match case in python
The match case contain of three main entities:
1. match: This is the keyword that starts the match-case statement.
2. case: This is the keyword that defines a case in the match-case statement.   
3. if: This is an optional keyword that can be used to add additional conditions to a case.

##%%%%%%%%%% LOOPS   %%%%%%%%%%%%##

FOR loop is used to iterate over a sequence (list, tuple, dictionary, set, or string) or other iterable objects.

While loop is used to execute a block of code repeatedly as long as a condition is true.
       $$$$$$  BREAK, CONTINUE, PASS  $$$$$$
       
###@@@@@@@@@ FUNCTIONS @@@@@@@@@###
# Functions are reusable blocks of code that perform a specific task.  
   $ Types of functions in Python: 
         1. Built-in functions: These are functions that are already defined in Python, such as print(), len(), type(), etc.
         2. User-defined functions: These are functions that are defined by the user to perform  
          --> define using the def keyword.
*** pass function is used to define a function without any code inside it. It is used as a placeholder for future code.  
       
&&  function Arguments and return values &&
    there are four types of function arguments in Python:
      1.Default arguments: These are arguments that have a default value if no value is passed to them when the function is called.
      2.Keyword arguments: These are arguments that are passed to a function by specifying the name of the argument and its value.
      3.Variable-length arguments: These are arguments that allow a function to accept a variable number of arguments.
      4.Required arguments: These are arguments that must be passed to a function when it is called. If they are not passed, an error will occur.       
       
    
#######     NUMPY TUTORIAL    #############

   Numpy is a general-purpose array-processing package. It provides a high-performance multidimensional array object and tools for working with these arrays. It is the fundamental  package for scientific computing with python. (((creating multi-D array  )))
     ** ARRAY::-->>
      An array is a data structure that stores values of same data type in Python
       
####### PANDAS  #############

 Pandas is an open sources. BSD-licensed library providing high- proformance, easy to use DS and Data analysis tools for the Python prog.. lang::

 Agenda
   => What is Data Frames?
     :---->A Data Frame is a two-dimensional data structure in Pandas, similar to an Excel spreadsheet or a table in a relational database. It consists of rows and columns, where each column represents a variable or field, and each row represents a single observation or record.
   => What is Data Series?
     ---->A Data Series is a one-dimensional labeled array of values, similar to a column in a spreadsheet or a table in a relational database. It is a single column of data with an index (row labels) and values.
   => Different operation in Pandas
        
        && Data Frame Operations::
      
      1. Filtering: Select rows based on conditions using the loc[] or iloc[] methods.
      2. Sorting: Sort rows by one or more columns using the sort_values() method.
      3. Grouping: Group rows by one or more columns and perform aggregation operations using the groupby() method.
      4. Merging: Combine two or more Data Frames based on a common column using the merge() method.
      5. Pivoting: Rotate a Data Frame from long format to wide format using the pivot_table() method.
       
       &&  Data Series Operations

      1. Indexing: Access individual elements using the loc[] or iloc[] methods.
      2. Slicing: Select a subset of elements using the loc[] or iloc[] methods.
      3. Mathematical Operations: Perform element-wise mathematical operations using various methods (e.g., add(), sub(), mul(), div()).
      4. Statistical Operations: Calculate summary statistics (e.g., mean, median, standard deviation) using various methods (e.g., mean(), median(), std()).

       ^%^%^%^%^%^%^%^%^ ENBUILT function.

 ## =====>> df= pd.read_csv('..')=> df.head()
 : csv basically use comma separated value..  df= pd.read_csv(['filepath or buffer' , "sep =','","header ='infer'",....])  
 ## ===> df.info: give the how namy columns, dtype,merory usage
 and index range..

 ## df.describe: it provide details like  what is the mean , count, min,std (column name..) of the column
cateogrial feature will be skip b/c can't find all these
 ## test_df=pd.read_csv('test1.csv',sep=';')    
 ## df['x0'].value_counts(): how many categories are present in different column....
 ## df[df['y']>100]: 
       
       %%%%%%%% CSV   %%%%%%%%%

       pd.read_csv: This is a pandas function that reads a CSV file into a DataFrame.

    inside csv we have seen that data is in this formate:
    data=('col1,col2,col3\n'
               'x,y,1\n'
               'a,b,2\n'
               'c,d,3') 
     type(data):: str
     
$$  StringIO =>text I/O implementation using an in memory buffer 

 (((code)))      pd.read_csv(StringIO(data)) 
   StringIO(data): This is a way to read the CSV data from a string. StringIO is a class from the io module that allows you to treat a string as a file-like object.  

##  Read from specific columns:::

df=pd.rea_csv(StringIO(data), usecols=lambda x:x.upper() in ['COL1','COL3']) ::::======>>
usecols=lambda x: x.upper() in ['COL1', 'COL3']: This is a lambda function that filters the columns to be read from the CSV file. Here's what it does:
x.upper(): This converts the column name to uppercase.
in ['COL1', 'COL3']: This checks if the uppercase column name is in the list ['COL1', 'COL3'].
lambda x: ...: This defines an anonymous function that takes a column name x as input and returns a boolean value indicating whether the column should be included.

((df.to_csv('Test.csv'))):: is used to save a Pandas DataFrame df to a CSV file named Test.csv
This will create a new file named Test.csv in the current working directory, containing the data from the df DataFrame

df=pd.rea_csv(StringIO(data),dtype=object)::
dtype=object, you're telling pandas to read all columns as objects, which means they will be stored as strings.c 

@@@@@@ now we specifying head of the column as differnt data type:
eg: df=pd.read_csv(StringIO(data),dtype={'b':int,'c':np.float((np=numpy(optional))),'a':'Int64'})

 #  CHECK the datatype
   df.dtypes(check all the columns of the datatype..)  

#   INDEX column and training delimiters......

 pd.read_csv(StringIO(data),index_col=0)
                           , index_col=2(3rd col become the index)

  === index_col=0 to indicate that the first column should be used as the index. pandas will automatically assign a numerical index to each row in the DataFrame, starting from 0.if we write index_col="False" it means that you don't want to use any column as the index of the DataFrame..

### ==>> Quoting and Escape Character. very useful in NLP

data='a,b\n"hello,\\"bob\\",nice to see you",5'
pd.read_csv(StringIO(data),escapechar='\\')::  escapechar='\\' tells Pandas to interpret backslashes (\) as escape characters.
This allows correct parsing of quoted strings with escaped characters, like \\" and \\.
This tells Pandas to interpret the backslash as an escape character, rather than a literal character.
O/P:	
                     a        b
hello,"bob",nice to see you   5

df=pd.read_csv('url link', sep='\t'): give all the data in table formate

         #######$$$$$$$$$$  READ JASON TO CSV
 data={"emp_name":"kirr","email":"kirr@34gmail.com","job_profile":[{"title1":"Team Leader","title2":"Manager","title3":"Sales man",}]}
 df1=pd.read_jason(data)
 df1.to_jason()

 o/p:::==>
   emp_name    email            job_profile
0  kirr     kirr@34gmail.com   {"title1":"Team Leader","title2":"Manager","title3":"Sales man"}
'{"emp_name":{"0":"Kirr"},"email":{"0":"kirr@34gmail.com"......}}
              ((key value pair makes.... with 0....))


df = pd.read_csv('..url....wine.data' , header=None)
df.head()

&&  TO convert jason to csv...

df.to_csv(wine.csv')
df.to_jason(orient="index")
df1.to_jason(orient="record"):they remove the key of the given o/p.. and give data in record wise....

orient parameter:: convert object into JASON. In this case, orient="index" means that each row will be represented as a JSON object with the index as the key. Other possible values for orient include "split", "records", "table", and "values", each of which produces a different format of JSON output.

                      ####   READING HTML technique
read html table into a list of dataframe objects...


url='....'
dfs = pd.read_html(url)
type(dfs) ## type is list

url_mcc="......"
dfs = pd.read_html(url_mcc , match='Country',header=0)

match='Country': This parameter specifies a string to search for in the HTML table headers. In this case, it's looking for tables with a header containing the word "Country".
header=0: This parameter specifies that the first row of the table should be used as the column headers.

                       ##########  READING EXCEL Files...

df_excel = pd.read_excel('Excel_sample.xlsx','sheet_name=0','header=0','dtype=None')
df_excel.head()

'sheet_name=0', but it should just be 0. This tells Python to read the first sheet in the Excel file
'header=0', but it should just be 0. This tells Python to use the first row of the Excel file as the column names.

                            #####  PICKLING......
All pandas objects are equipped with to_pickel methods which use python's module to save DS to disk
Pickling is a process in Python that allows you to serialize and de-serialize Python objects, such as data structures, functions, and even entire programs. This can be useful for storing and retrieving data, as well as for distributing Python objects across different systems.


# # import pickle
# # # Create a Python object
# # data = {'name': 'John', 'age': 30}
# # # Pickle the object
# # pickled_data = pickle.dumps(data)
# # # Print the pickled data
# # print(pickled_data)
                                            or
  df_excel.to_pickel('df_excel')  ### convert...and save 
  df=pd.read_pickel('df_excel')
  df.head()     

  ////////////////////////////////////////////////////////////////////

       MATPLOTLIB Tutorial....

Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
Matplotlib is a powerful and versatile open-source plotting library for Python, designed to help users visualize data in a variety of formats. 
Some major pros of Matplotlib are::::==>
 used to create graphs and charts. Whether you're drawing a line graph, a bar chart, a histogram, or even a 3D plot
 Great control of every element in a figure
 High quality O/P in many formats
 Very customizable in general      


















'''
