import time

tup1 = ('physics', 'chemistry', 1997, 2000,)
tup2 = (1, 2, 3, 4, 5, 6, 7,)
print("tup1[0]: ", tup1[0])
print("tup2[1:5]: ", tup2[1:5])

ticks = time.time()
print('\nThe time since the epoch is given as: '
      '\n\t{}'.format(ticks))

localtime = time.localtime()
print(localtime)

'''Any set of multiple objects, comma-separated,
written without identifying symbols,
i.e., brackets for lists, parentheses for tuples, etc.,
default to tuples. example below'''

sam = 'abc', -4.24e93, 18 + 6.6j, 'xyz'
print(sam)
print(type(sam))

tuple1, tuple2 = (123, 'xyz'), (456, 'abc')
print(tuple1, tuple2)
totaltuple = zip(tup1, tup2)
print(totaltuple, '\n')

dictsam = {'name': 'ernest lipson', 'age': 12, 'class': 'level 200'}
print('dictsam[name]:', dictsam['name'])
print('dictsam[age]:', dictsam['age'])

identifier = {'Name': 'Zara', 'Age': 8,
              'Class': 'First', 'School': "DPS School"}
print(identifier)

dict2 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# remove entry with key 'Name'
del dict2['Name']
# remove all entries in dict
dict2.clear()
# delete entire dictionary
del dict2

# dictionary properties
'''More than one entry per key not allowed.
Which means no duplicate key is allowed.
When duplicate keys encountered during assignment,
the last assignment wins'''

dictA = {'name': 'Zara', 'Age': 7, 'identity': 'Manni'}
print("dict['Name']: ", dictA['name'], '\n')


def printme(string):
    """This prints a passed string to the function"""
    print(string)


printme("This is the first call to this defined function!")
printme("Again second call to the same function")


def changename(peop):
    """This changes a list passed into it"""
    peop.append([23, 15, 18, 99.87])
    return '\nThe new liist function is:' \
           '\n\t {}'.format(peop)


mylist = [17, 19.89, 88, 35, 78]
print(changename(mylist))
# using keyword arguments
print(changename(peop=[43, 78.8, 12, 56, 109]))


def printinfo(xname, age):
    """This prints a passed info to this function"""
    print("Name: ", xname)
    print("Age: ", age)
    return xname, age


# Now you can call printinfo function
printinfo(age=50, xname="miki")


# default arguments
def mydetails(nme, age, sch='knust'):
    """this prints my info"""
    details = [nme, age, sch]
    print(details)


mydetails('ernest lipson', 23)

# variable length arguments
'''You may need to process a function for more arguments
than you specified while defining the function.
These arguments are called variable-length arguments
and are not named in the function definition,
unlike required and default arguments.
An asterisk (*) is placed before the variable name that
holds the values of all non-keyword variable arguments.'''


def var_info(arg, *vartuple):
    print('The value representing the firsr'
          'argument is {}'.format(arg))
    print(list(vartuple))


var_info(12, 67, 'lipson', 'ubuntu', 89.44)

# using the global key word variable.
Money = 2000


def add_money():
    global Money
    Money = Money + 1


print(Money)
add_money()
print(Money)

num = int(input('\nplease enter number: '))
while num < 0 or num == 0:
    if num == 0:
        print('TraceBack: value input error')
        num = int(input('\nplease enter number: '))
    elif num < 0:
        print('please input +ve values ')
        num = int(input('\nplease enter number: '))
else:
    if num % 2 == 0:
        print('Number given is even')
    elif num % 2 == 1:
        print('number given maybe odd')
    else:
        print('cant determine number')


# turning the above code into a function
def even_odd(number=int(input('\nplease enter number: '))):
    """
    function to determine if a given number is even or odd
    """
    while number < 0 or number == 0:
        if number == 0:
            print('TraceBack: value input error')
            number = int(input('\nplease enter number: '))
        elif number < 0:
            print('please input +ve values ')
            number = int(input('\nplease enter number: '))
    else:
        if number % 2 == 0:
            print('Number given is even')
        elif number % 2 == 1:
            print('number given maybe odd')
        else:
            print('cant determine number')


even_odd()

print(' ')


def display_info(work=input('please what is your work: '),
                 age=int(input('please age must be more than 18: ')),
                 yname=input('please input your name: ')):
    """function to display name and age"""
    while age or yname or work:
        if age <= 18:
            print('You are not elligible to participate')
            break
        else:
            print(f'your work is {work.capitalize()}, '
                  f'name is {yname.capitalize()} and age is {age}'.title())
            break


display_info()

text = input('please input text you want printed: ')


def make_shirt(size, atext):
    """to make a shirt"""
    print(f'the size of your shirt is {size} and the message '
          f'printed on it is {atext}')


make_shirt(18, text)
make_shirt(atext=text, size=94)


# using default positional parameters
def make_shirt(btext, size=100):
    """to make a shirt"""
    print(f'the size of your shirt is {size} and the message '
          f'printed on it is {btext}')


make_shirt(text)


# returning values of a function


def get_name(fname, lname):
    """returns formatted name passed"""
    fullname = f'{fname} {lname}'
    return fullname.title()


name = get_name('mensah', 'ghartey')
print(name)
print(get_name('mensah', 'joe wise'))


def get_formatted_name(first_name, last_name, middle_name=''):
    """return a full name fullt formatted"""
    if middle_name:
        fullname = f'\n{first_name.title()} ' \
                   f'{middle_name.title()} ' \
                   f'{last_name.title()}'
    else:
        fullname = f'{first_name.title()}' \
                   f' {last_name.title()}'
    return fullname


newname = get_formatted_name('lipson', 'kwabena', 'boateng')
print(newname)
name_two = get_formatted_name('ernest', 'ayew')
print(name_two)
