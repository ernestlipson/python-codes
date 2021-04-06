#!/usr/bin/env python
# coding: utf-8

# ### What can Python do?
# 
#     Python can be used on a server to create web applications.
#     Python can be used alongside software to create workflows.
#     Python can connect to database systems. It can also read and modify files.
#     Python can be used to handle big data and perform complex mathematics.
#     Python can be used for rapid prototyping, or for production-ready software development.
# 
# ### Why Python?
# 
# Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc). Python runs on an interpreter system,
# meaning that code can be executed as soon as it is written. This means that prototyping can be very quick. Python
# can be treated in a procedural way, an object-orientated way or a functional way Python relies on indentation,
# using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages
# often use curly-brackets for this purpose.
#     
# ### Multi Line Comments
# 
# Python does not really have a syntax for multi line comments. To add a multiline comment you could insert a # for
# each line: Or, not quite as intended, you can use a multiline string. Since Python will ignore string literals that
# are not assigned to a variable, you can  add a multiline string (triple quotes) in your code, and place your
# comment inside it: As long as the string is not assigned to a variable, Python will read the code, but then ignore
# it, and you have made a multiline comment.
# 

# In[7]:


# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

# The Python print statement is often used to output variables.
# To combine both text and a variable, Python uses the + character
x = "awesome"
print("Python is " + x)
x = "Python is "
y = "awesome"
z = x + y
print(z)

'''If you create a variable with the same name inside a function, 
this variable will be local, and can only be used inside the function. 
The global variable with the same name will remain as it was,
global and with the original value.'''

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()
print("Python is " + x)


# Normally, when you create a variable inside a function,
# that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
    global x
    x = "fantastic"


myfunc()
print("Python is " + x)

# Also, use the global keyword if you want to change a global variable inside a function.
# To change the value of a global variable inside a function,
# refer to the variable by using the global keyword:

x = "awesome"


def myfunc():
    global x
    x = "fantastic"


myfunc()
print("Python is " + x)

# ### Built-in Data Types
#     Text Type: => 	str
#     Numeric Types: =>	int, float, complex
#     Sequence Types: =>	list, tuple, range
#     Mapping Type: =>	dict
#     Set Types: =>  set, frozenset
#     Boolean Type: =>	bool
#     Binary Types: =>	bytes, bytearray, memoryview
#     
#     Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
#     Float can also be scientific numbers with an "e" to indicate the power of 10.

# In[1]:


xlab = int(5)
print(type(xlab))

xcom = 1j
print(type(xcom))

x = set(('apple', 'banana', 'mongoDB'))
print(x)
print(type(x))

bfloat = 54e7  # Float can also be scientific numbers with an "e"
# to indicate the power of 10.
print(bfloat)

# In[2]:


# type conversion
x, y, z = 1, 2.8, 1j

a = float(x)
b = int(y)
c = complex(a)

print(a, b, c)
# You cannot convert complex types into another number type.


# ### Random Number
# 
#     Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

# In[7]:


# generating a random Number
import random as r

print(r.randrange(1, 10))

# In[10]:


from random import *

print(randrange(2, 20))

# In[16]:


from random import randrange

print(randrange(1, 14))

# ### Strings are Arrays in Python
# 
#     Like many other popular programming languages, strings in Python are arrays of 
#     bytes representing unicode characters.
#     However, Python does not have a character data type, a single character 
#     is simply a string with a length of 1.
#     Square brackets can be used to access elements of the string.

# In[17]:


a = 'hello python'
print(a[7])

# slicing
# You can return a range of characters by using the slice syntax.
b = 'yeah python'
print(b[2:4])
print(b[-5:-1])

# String Length
# To get the length of a string, use the len() function.
print(len(b))

# String Methods
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

# The split() method splits the string into substrings 
# if it finds instances of the separator:
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

# To check if a certain phrase or character is present in a string, 
# we can use the keywords in or not in.
# Check if the phrase "ain" is present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
print(x)

# Check if the phrase "ain" is NOT present in the following text:
txt = "The rain in Spain stays mainly in the plain"
x = "ain" not in txt
print(x)

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)

# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# ### String Format
# 
#     We cannot combine strings and numbers like this:
#     age = 36
#     txt = "My name is John, I am " + age
#     print(txt)
#     
#     But we can combine strings and numbers by using the format() method!
#     The format() method takes the passed arguments, formats them, 
#     and places them in the string where the placeholders {} are.
#    ### Use the format() method to insert numbers into strings:
#     age = 36
#     txt = "My name is John, and I am {}"
#     print(txt.format(age))
#     The format() method takes unlimited number of arguments, 
#     and are placed into the respective placeholders:
#     You can use indexes numbers {0} to be sure the arguments are placed 
#     in the correct placeholders.

# In[19]:


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# example 2:
height = 78.19
bmi = 16.19
name = 'ernest lipson'
info = 'My name is {}, I am {} in height and {} in weight'
print(info.format(name, height, bmi))

# In[20]:


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item ie. {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# In[43]:


# You can use indexes numbers {0} to be sure the arguments 
# are placed in the correct placeholders.
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# In[44]:


# example 2
bot = 18.199
rel = 78
price = 19
need = 'I want {2} bags of rice, {0} per bag and {1} bottles of wine'
print(need.format(bot, rel, price))

# ### Escape Character
# 
#     To insert characters that are illegal in a string, use an escape character.
#     An escape character is a backslash \ followed by the character you want to insert.
#     An example of an illegal character is a double quote ("") inside a string 
#     that is surrounded by double quotes.
#     
#     Example
#     You will get an error if you use double quotes inside a string 
#     that is surrounded by double quotes:
#     
#     txt = "We are the so-called "Vikings" from the north."
#     To fix this problem, use the escape character \":
#     
#     Example
#     The escape character allows you to use double quotes when you 
#     normally would not be allowed:
#     
#     txt = "We are the so-called \"Vikings\" from the north."

# In[22]:


# txtA = "We are the so-called "Vikings" from the north."
txtB = "We are the so-called \"Vikings\" from the north."
print(txtB)

# In[23]:


# binary, hexadicimal numbers
a = 0b11010
b = 0xb65f
c = 0b1111
print(a, b, c)

# ### Python Booleans
#     The bool() function allows you to evaluate any value, 
#     and give you True or False in return,
#     
#     Evaluate a string and a number:
#     print(bool("Hello"))
#     print(bool(15))
#     print(bool('everyone'))
#     
#     All the above code returns true if evaluated
#     Most Values are True
# 
#     Almost any value is evaluated to True if it has some sort of content.
#     Any string is True, except empty strings.
#     Any number is True, except 0.
#     Any list, tuple, set, and dictionary are True, except empty ones.
#     In fact, there are not many values that evaluates to False, except empty values, 
#     such as (), [], {}, "", the number 0, and the value None. 
#     And of course the value False evaluates to False.
#     Python also has many built-in functions that returns a boolean value, 
#     like the isinstance() function, which can be used to determine if an 
#     object is of a certain data type:
#     
#     Example
#     Check if an object is an integer or not:
#         isinstance(x, int)

# In[28]:


print(bool(['work', 'assumption']))
print(bool([]))
x = 200
mol = 'mol index of 50g'
print(isinstance(x, float))
print(isinstance(x, int))
print(isinstance(mol, str))

# ### Python Identity Operators
# 
#     Identity operators are used to compare the objects, not if they are equal, 
#     but if they are actually the same object, with the same memory location:
# 
#     is:  	Returns true if both variables are the same object 	
#     is not: 	Returns true if both variables are not the same object

# In[14]:


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x, and has the same memory location
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": 
# this comparison returns True because x is equal to y


# In[1]:


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": 
# this comparison returns False because x is equal to y


# ### Python Membership Operators
# 
#     Membership operators are used to test if a sequence is presented in an object:
#     
#     in : Returns True if a sequence with the specified value is present in the object
#     not in: Returns True if a sequence with the specified value is not present 
#     in the object

# In[29]:


x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list

x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list

x = ('mana', 'bread', 99.56)
print('bread' not in x)
# returns False because a sequence with the value 'bread' is in the list


# ### Python Bitwise Operators
#     Bitwise operators are used to compare (binary) numbers:
#     
#     &  ---- Sets each bit to 1 if both bits are 1
#     
#     | ----	Sets each bit to 1 if one of two bits is 1
#     
#     ^ ----  Sets each bit to 1 if only one of two bits is 1
#     
#     ~ ----  Inverts all the bits
#     
#     << ---- Zero fill left shift; Shift left by pushing zeros in 
#             from the right and let the leftmost bits fall off
#             
#     >> ---- Signed right shift; Shift right by pushing copies 
#             of the leftmost bit in from the left, and let the rightmost bits fall off

# In[42]:


bit = 5 & 6 & 7
print(bit)

bitwise = 5 | 6
print(bitwise)

sets = 8 ^ 9
print(sets)

gyt = ~3
print(gyt)

tri = 5 << 4
print(tri)

ned = 6 >> 3
print(ned)

# ### Python Collections (Arrays)
# 
#     There are four collection data types in the Python programming language:
# 
#     List: is a collection which is ordered and changeable. Allows duplicate members.
#     Tuple: is a collection which is ordered and unchangeable. Allows duplicate members.
#     Set: is a collection which is unordered and unindexed. No duplicate members.
#     Dictionary: is a collection which is unordered, changeable and indexed. No duplicate members.
# 
# ### The extend() method
#     adds the specified list elements (or any iterable) to the end of the current list.
#     
#     list.extend(iterable)
#     parameter needed: Any iterable (list, set, tuple, etc.)
#     
#     Add a tuple to the fruits list:

# In[39]:


# the extend() metheod
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)

# ### The sort() method sorts the list ascending by default.
# 
#     You can also make a function to decide the sorting criteria(s).
#     list.sort(reverse=True|False, key=myFunc)

# In[47]:


cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# In[43]:


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# Negative indexing means starting from the end of the list.
# This example returns the items from index -4 (included) to index -1 (excluded)
# Remember that the last item has the index -1

# changing item value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# looping theough a list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for e in thislist:
    print(e, end=" ")

# Check if "apple" is present in the list:
if 'apple' in thislist:
    print('\nYES')

print(len(thislist))
thislist.append('pineapple')
thislist.insert(2, 'berry')

print(thislist)
thislist.remove('kiwi')
print(thislist)
thislist.pop(4)
print(thislist)

# The del keyword removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely:
thislist = ["apple", "banana", "cherry"]
del thislist

# The clear() method empties the list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist.clear()
print(thislist)

# to copy a list
# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
newlist = list(thislist)

# Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Append list2 into list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
    list1.append(x)
print(list1)

# the append method
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)

ManyPle = ['array', 'List', 'Tuple', 'Dictionary']
FewPle = [2, 4, 18, 19, 34.9]
for e in ManyPle:
    FewPle.append(e)
print(FewPle)

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)

# the count method
# Return the number of times the value "cherry" appears in the fruits list:
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

fruits = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = fruits.count(9)
print(x)

fruits.reverse()
fruits.sort()
print(fruits)

# The buil-in function reversed() returns a reversed iterator object.
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
    print(x, end=' ')

# ### Tuples
#     A tuple is a sequence which is ordered and unchangeable.
#     Once a tuple is created, you cannot change its values. Tuples are unchangeable, 
#     or immutable as it also is called.
#     But there is a workaround. You can convert the tuple into a list, 
#     change the list, and convert the list back into a tuple.
#     
#     To create a tuple with only one item, you have add a comma after the item, 
#     unless Python will not recognize the variable as a tuple.
#     
#     You cannot remove items in a tuple.
#     Tuples are unchangeable, so you cannot remove items from it, 
#     but you can delete the tuple completely:

# In[49]:


this_tuple = ('apple', 'banana', 'cherry', 'yummy',)
print(this_tuple)
print(this_tuple[2])
print(this_tuple[-2])

# changing the value of a tuple.
xlist = ('apple', 'banana', 'cherry',)
ylist = list(xlist)
ylist[2] = 'berry'
xlist = tuple(ylist)
print(xlist)

# printing the values in a tuple
for e in this_tuple:
    print(e, end=' ')
print('\n', len(this_tuple))

# creating a single item tuple
xtuple = ('bottles',)
print(type(xtuple))
ytuple = ('container',)
print(type(ytuple))




newTuple = zip(thisTuple, xlist)
print(newTuple)

yem = tuple(('many_ace', 'tantra', 'mile_7',))
print(yem)


# In[48]:


# python functions, factorial function
def fac(num):
    if num == 1:
        return 1
    else:
        return num * fac(num - 1)


print(fac(9))

# In[ ]:
