print('hello world')
message = 'many working generations'
print(message)

name = 'ada lovelace'
# title method returns title of string given
print(name.title())
print(name.upper())
print(name.lower())

fname = 'ernesta'
lname = 'darko owusu'
allname = f'{fname} {lname}'

print(allname)
# more code editting with format
print(f'hello, {allname.title()} !')

'''or assign message to a variable'''
name = f'Many nations, {lname.title()}'
print(name)

# using  python 3.5 version
allname = '{} {}'.format(fname, lname)
print(allname)
'''To use format(), list the variables you want to use 
in the string inside the parentheses following format.
Each variable is referred to by a set of braces; 
the braces will be filled by the values
listed in parentheses in the order provided'''

print('Languages:\n\t\tPython\n\t\tJava\n\t\tjavaScript')

# To ensure that no whitespace exists at the right end of a string,
# use the rstrip() method.
language = '    python_language    '
print(language)
language.rstrip()
print(language)
print(language.lstrip())
print(language.strip())

author = 'Albert Einstein'
qoute = 'once said, "A person who never made a mistake'
cont = 'never tried anything new"'
zipstatement = zip(qoute, cont)
print(zipstatement)

qc = '{} {} {}'.format(author, qoute, cont)
print(qc)

'''when you are writting long numbers in python, you can group
digits using underscores to make large numbers more readable.'''
universe = 14_000_000_000
print(universe)

# making lists
car_brands = ['vw', 'kantanka', 'opel', 'nissan']
print(car_brands)

# accessing elements in a list
print(car_brands[3].title())
message = f'my first bicycle was a {car_brands[1].title()} model'
print(message)

names = ['james', 'oppong', 'emmanuella', 'charity']
newName = ''
for i in names:
    i = newName

print(f"My friend is {names[1].title()}")
# modifying List elements
names[3] = 'adade'
print(names)
names.append('kwame')
print(names)

# inserting new elements into a list
names.insert(2, 'evelyn')
print(names)

# deleting elements
del names[2]
print(names)
# you can no longer access the value that was removed
# from the list after the del statement is used.

newList = names.pop()
print(names)
# The pop() method removes the last item in a list,
# but it lets you work with that item after removing it

print(newList)
print(f'The best of my friends is {newList.title()}')
# the pop method can remove any item in a list by specifying the
# index of the item you want to remove
newList = names.pop(2)
print(newList)

# using the remove method
names.remove('oppong')
'''The remove() method deletes only the first occurrence 
of the value you specify. If there’s a possibility the value 
appears more than once in the list, you’ll need to use a loop
to make sure all occurrences of the value are removed.'''
