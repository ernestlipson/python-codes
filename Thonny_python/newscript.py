import os


def myfunc():
    global x
    x = 'fantastic'
    print('python is ' + x)

# because of the use of the keyword global, variable x can
# be used outside the function.


myfunc()
print('python  is ' + x)

# strings are arrays in python
a = 'School re-opening begins shortly'
for i in a[0:1]:
    global b
    b = a.replace('e', 'a')
    print(b)
for e in a[0:1]:
    g = a.split('o')
    print(g)
for i in a[0:1]:
    if 's' or 'a' in a:
        print('TRUE')
    elif 'b' and 'l' not in a:
        print('TRUE')
    else:
        new_a = a[:]
        print(new_a)
if a[12] == 't':
    print('its inside')
else:
    print('cannot be found')
print(a[1:8].upper())
print(b)

'''string concatenation'''
a = 'when is school re-opening!'
b = ' maybe next week?'
print(a + b)

# formatting documents
age = 36
txt = 'My name is John Kumah, I am {}'
final = txt.format(age)
print(final)

# example 2:
height = 78.19
bmi = 16.19
name = 'ernest lipson'
info = 'My name is {}, I am {} in height and {} in weight'
print(info.format(name, height, bmi))

quantity = 78
price = 12.8
item_no = 889
my_order = 'I want {2} of price {1} and a quantity of {0}'
print(my_order.format(quantity, price, item_no))
print(my_order.format(item_no, quantity, price))

print(bool('Hello'))
print(bool(15))
print(bool('everyone'))

thislist = ["apple", "banana", "cherry",
            "orange", "kiwi", "melon", "mango"]

print(thislist[-4:-1])
print(thislist[2:-1])

for i in thislist:
    print(i[:4], end=' \t')

if 'apple' in thislist:
    print('\nYES')
else:
    print("MANY NO's")

# copying a list from one list to another
anotherList = thislist[:]
# copying a list from one list to another using append
newList = []
for i in anotherList:
    newList.append(i)

print('\n\t{}'.format(anotherList))
print('\n\t{}'.format(newList))


def copylist(list_args=None, nlist=None):
    """copy a list from one list to another,
    ie. copies list from list_args to nlist"""
    if nlist is None:
        nlist = []
    if list_args is None:
        list_args = []
    for copy in list_args:
        nlist.append(copy)

    return nlist


copying = []
print(copylist(anotherList, copying))
# newCopy = copylist(list('string concatenation'))
# print(newCopy)

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)
print(copylist(a, b))
a.extend(b)
print(a)

toli = a.count("apple")
print(toli)

alph = ["a", "b", "c", "d"]
reversed(alph)
print(alph)
alph.reverse()
print(alph)

this_tuple = ('apple', 'banana', 'cherry', 'yummy')
print(this_tuple)
print(this_tuple[2])
print(this_tuple[-2])

# changing the value of a tuple.
xlist = ('apple', 'banana', 'cherry',)
ylist = list(xlist)
ylist[2] = 'berry'
xlist = tuple(ylist)
print(xlist)

for e in this_tuple:
    print(e, end=' ')
print('\n', len(this_tuple))


data_file = {91.8: 'kumerica', 12: 'achimota', 'affirm': 0}
town = 'general'

new_dict = {town: data_file}
print(new_dict[town][91.8])

# swapping two variables
a, b = 10, 12
print(a, b)

a, b = b, a
print(a, b)

# program to check if a given number is positive or negative.
dvar = int(input('please input a number: '))
if dvar < 0:
    print('Number given is negative')
elif dvar == 0:
    while dvar == 0:
        print('cannot accept 0 inputs')
        dvar = int(input('please input a number: '))
else:
    print('Number given is positive')

print(os.getcwd())
