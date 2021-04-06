# ranging of values of values
num = []
for i in range(1, 10):
    num.append(i)

print(num)

numbers = list(range(10))
print(numbers)
numbers = list(range(2, 11, 2))
print(numbers)

# making a list of the first 10 square numbers,
# that is, the square of each integer from 1 through 10
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
listdigits = [min(digits), max(digits), sum(digits)]
print(listdigits)

sqrlist = []
for i in range(1, 19):
    sqrlist.append(i ** 2)

print(sqrlist)

'''list comprehension: A list comprehension combines 
the for loop and the creation of new elements into one line, 
and automatically appends each new element'''
squares = [value ** 2 for value in range(1, 12)]
print('\nLIST COMPREHENSION TEST \n{}'.format(squares))

# finding sum of values
number = [e for e in range(1, 10000000)]
print('\nSum of numbers from 1 to 10e is {}'.format(len(number)))

listmill = []
for value in range(1, 1_000_0001):
    listmill.append(value)
print(len(listmill))

for i in range(20):
    if i % 2 == 1:
        print(i, end=' ')
    else:
        continue

# List Comprehension
value = [f ** 3 for f in range(1, 10)]
value = list(value)
print(' \n \n{}'.format(value))

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[-3:])
'''You can include a third value in the brackets 
indicating a slice. If a third value is
included, this tells Python how many items 
to skip between items in the specified range.'''

# you can use a slice in a for loop to loop
# through a subset of elements
print('\nthe first three players on my team: '.title())
for p in players[:3]:
    print(f'\t{p}')

# copying a list
my_foods = ['pizza', 'falafel', 'carrot']
friend_foods = my_foods[:]
print('my favourite foods')
print(my_foods)
print('\nMy friends favourite foods')
print(friend_foods)

# Tuples
'''you can assign a new value to a variable that
represents a tuple'''
dim = (100, 200, 56,)
print('original dimensions')
for d in dim:
    print(f'\t{d}')

dim = (400, 900, 78,)
# reassigning tiple variables is valid
print('\nModified dimensions')
for m in dim:
    print(f'\t{m}')

buffet = ('waakye', 'omotuo', 'kpanla', 'aky3ke',)
print('\nItems in buffet are:')
for b in buffet:
    print(f'\t{b}')

# moddifying the values of a tuple
buffet = list(buffet)
buffet.append('samosa')
buffet = tuple(buffet)
print(f'\nitems in modified lists are: ')
for e in buffet:
    print(f'\t{e}')


# using if statements
cars = ['audi', 'bmw', 'subaru', 'toyota', 'opel-astra']
for c in cars:
    if c == 'bmw':
        print(c.upper())
    else:
        print(c.title())

# conditinal tests for if statements
request = 'mushrooms'
if request != 'anchovies':
    print('\nhold the anchovies!'.capitalize())

# checking whether a value is not in a list
banned = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned:
    print(f'{user.title()}, you cannot access the portal' ''
          'your name is not on our file system')

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# if...elif statements
age = 70
price = 0

if age < 18:
    price = 0
elif age == 18:
    price = 25
elif age >= 65:
    price = 40

print(f'\nyour admission cost is ${price}')

# Testing Multiple Conditions
topping = ['mushrooms', 'cheese', 'yoghurt']
if 'mushrooms' in topping:
    print('adding mushrooms')
if 'cheese' in topping:
    print('adding cheese')
if 'strawberry' in topping:
    print('adding yoghurt')

print('\nFinished making your pizza!'''
      'your pizza contains: ')
for i in topping:
    print(f'\t{i}')
print(topping)

alien = 'green'
if alien == 'green':
    print('earned 5 points')

# checking for special items
requested = topping[:]
for requested in requested:
    print(f'Adding {requested}')

print('\nfinished making your Pizza')

requested = topping[:]
for requested in requested:
    if requested == 'mushrooms':
        print('\nsorry out of mushrooms')
    else:
        print(f'Adding {requested}')

print('\nfinished making your Pizza')

# Checking That a List Is Not Empty before...
requested = []
if requested:
    for requested in requested:
        if requested == 'cheese':
            print('\nsorry out of cheese')
        else:
            print(f'\nAdding {requested}')
else:
    print('\nPizza items is empty')

# using multiple Lists to create the pizza
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese', 'red fish']

for r in requested_toppings:
    if r in available_toppings:
        print(f"Adding {r}.")

    else:
        print(f"Sorry, we don't have {r}.")
print("\nFinished making your pizza!")
print('your pizza is {}'.capitalize().format(r))


# Assignment (Try it yourself)
username = ['admin', '@ernestlipson', 'evanda', 'pretty', 'kalif']

if username:
    for u in username:
        if u == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {u} welcome to this site')
else:
    print('\nNo users found')

# How websiites ensure that each user has a unique username
current_users = username[:]
new_users = ['agyeman', 'mireku', 'evanda', '@ernestlipson', 'evelyn']
for n in new_users:
    if n in current_users:
        print('Enter a new username please !')
    else:
        print('username is available')

print(' ')

# Ordinal Numbers and their positions
ordinal = [i for i in range(1, 10)]
print('Ordinal Numbers and their positions')
for i in ordinal:
    if i == 1:
        print('\t1st')
    elif i == 2:
        print('\t2nd')
    elif i == 3:
        print('\t3rd')
    elif i > 3:
        print(f'\t{i}th')
