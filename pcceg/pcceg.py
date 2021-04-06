print('hello world')
message = 'many working generations'
print(message)

name = 'ada lovelace'
print(name.title())
# the title method returns title of string given
print(name.capitalize())
print(name.upper())
print(name.lower())

fname = 'ernest'
lname = 'darko owusu'
allname = fname + " " + lname
print(allname)

# more code editting with format
print(f'hello, {allname.title()} !')
'''or assign message to a variable'''
name = f'Many nations, {lname.title()}'
print(name)

# using  python 3.5 version mode formatting
allname = '{} {}'.format(fname, lname)
print(allname)
'''To use format(), list the variables you want to use 
in the string inside the parentheses following format.
Each variable is referred to by a set of braces; 
the braces will be filled by the values
listed in parentheses in the order provided'''

python = 'magic python'
version = 3.9
new_name = 'working on this python script with name {} and id {}'.format(
    python, version
)
print(f'\n{new_name}')
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
newName = []
for i in names:
    newName.append(i)

    print(i)
    print(newName)
print(newName)

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
'''you can no longer access the value that was removed
from the list after the del statement is used.'''

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

dinner_list = ['quansah', 'james-ansah', 'darko', 'ahmad']
for i in dinner_list:
    print(f'Please Mr {i} you are invited to the state dinner.')
print(f'{dinner_list[-1].capitalize()} said he cant make it')

dinner_list[-1] = 'shatta'
print(f'\nMr {dinner_list[-1].capitalize()} is now invited to the dinner')

print('\nA big dinner table has been set so more members! right')
dinner_list.append('kofi mole'.title())
dinner_list.insert(0, 'james-mireku'.title())
dinner_list.insert(2, 'frimpong boateng'.title())

print(dinner_list)
last = dinner_list.pop(-1)
last2 = dinner_list.pop(-2)
last3 = dinner_list.pop(-3)
last4 = dinner_list.pop(-4)
# print(f'Mr(s) {last}, {last2}, {last3}, {last4},', end=' ')
print('\nMr(s) {}, {}, {}, {} your invitation is revoked'.format(
    last.title(), last2.title(), last3.title(), last4.title()
))
# print('your invitation is revoked')

for i in dinner_list:
    print(i, end=' , ')
    # printing list of items on the same line
dinner_list.reverse()
print(f'\n{dinner_list}')

'''organizing Lists The sort() method, changes the order
of the list perma-nently'''

dinner_list = ['quansah', 'james-ansah', 'darko', 'ahmad']
dinner_list.sort()
print('\n\n{}'.format(dinner_list))

# sorting the list in reverse alphabetical order
dinner_list.sort(reverse=True)
print(dinner_list)

# list can be sorted temporarily with the sorted() method
cars = ['bmw', 'hyundai', 'toyota', 'opel']
print(sorted(cars, reverse=True))
# reversing the order of a list
cars.reverse()
print(cars)

# the reverse method doesnt sort backwards alphabetically,
# it simply reverses the order
location = ['los angels', 'Hauwei', 'Hong-kong', 'Berlin']
new_location = []
for i in location:
    new_location.append(i)
    print(new_location)

print(' ')

print(sorted(location))
print(location)
print(sorted(location, reverse=True))
location.reverse()
print(location)
for location in location:
    print(location)

print(' ')

magicians = ['David Copperfield', 'Apollo Robbins',
             'David Devant', 'Shin Lim', 'Lance Burton',
             'David Blaine']
for magicians in magicians:
    print(f'{magicians.title()} that was a greak trick')
    print(f"I can't wait to see your next trick, {magicians.title()}.\n")
print(f'Thank you all magicians, it was a great show')

print(magicians.title())

pizza = ['Pepperoni', 'Mushrooms', 'Onions',
         'Sausage', 'Bacon', 'Extra cheese',
         'Black olives', 'Green peppers']
for p in pizza:
    print(f'I like {p.title()} a lot, TASTY!.\n')

fri_pizza = pizza[:]
fri_pizza.append('meat bag')
pizza.append('chicken')
print(fri_pizza, pizza)
