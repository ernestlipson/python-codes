juliet = {
    'first_name': 'Adams smith',
    'school': 'st johns grammer',
    'age': 22,
}
evans = {
    'first_name': 'evans opoku',
    'school': 'west africa',
    'age': 26
}
people = [juliet, evans]
for i in people:
    print(i)
school = input('the name of the school is: ')
print(f'\nthe name of the school is {school}')

# Sometimes you’ll want to write a prompt that’s longer
# than one line. You can assign your prompt to a variable and
# pass that variable to the input() function

prompt = "\nIf you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f'\nHello, {name}')

height = int(input('\nplease input your height: \n'))
if height >= 48:
    print('you can ride roller coaster')
elif height <= 47:
    print('may be next year')

# determining if number is even or odd
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

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ' '
while message != 'quit':
    message = input(f'\n{prompt}')
    if message != 'quit':
        print(message)
# adding flags to a program, below program performs similarly
# like the above code
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# using break statements in code
prompt = '\nPlease enter the name of a city you have visited: '
prompt += '\n(Enter quit when done) '
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f'I would love to go to {city.title()}!')

# using the continue statement, printing odd numbers
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# loops with Lists and Dictionaries
users = ['abena', 'nyamesem', 'frema opare']
new_users = []
while users:
    current_user = users.pop()
    print(f"verifying user: {current_user.title()}")
    new_users.append(current_user)
print('\nThe following users have been confirmed: ')
for u in new_users:
    print(u.title())
# Removing All Instances of Specific Values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(f'\n{pets}')

while 'cat' in pets:
    pets.remove('cat')
print(pets)

# Filling a Dictionary with User Input
response = {}
# Set a flag to indicate that polling is active.
polling_active = True
while polling_active:
    name = input('\nWhat is your name: ')
    name2 = input('Where do you intend going: ')

    response[name] = name2
    repeat = input("Would you like to let another person respond?"
                   " (yes/ no) ")
    if repeat == "no":
        polling_active = False
print(f'\n{response}')

print("\n--- Poll Results ---")
for name, response in response.items():
    print(f"{name} would like to climb {response}.")
print('')


def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


greet_user('jesse')


def favorite_book(title):
    '''displays title of a book'''
    print(f'one of my favourite books is {title}')


favorite_book('Alice wonderland')


def animal(type, name):
    """describes animal type and name"""
    print(f'I have a {type}')
    print(f'My {type}\'s name is {name}')


animal('fowls', 'meneku')


def function(x, y):
    """fxn to add two numbers"""
    return x + y


summf = function(y=8, x=12)
print(summf)


def display_info(work, age, ple):
    """dunction to display name and age"""
    age = input('please age must be more than 18: ')

    print(f'your work is {work}, name is {ple} and age is {age}')


display_info('developer', 18, 'ernest lipson')


def describe_pet(animal_type, pet_name):
    """Display information about a pet."""

    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')
# both function calls above are equivalent


def describee_pet(self, parameter_list='dog'):
    """function to name animal type setting default value to dog"""
    print(f'\nI have animal {self}')
    print(f'My animals name is {parameter_list}')


describee_pet('cow')

# Avoiding Argument Errors
# Unmatched arguments occur when you
# provide fewer or more arguments than a function needs to do its work.
text = input('please input text you want printed')


def make_shirt(size, text):
    """to make a shirt"""
    print(f'the size of your shirt is {size} and the message'
          f'printed on it is {text}')


make_shirt(18, text)


def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# making an argument optional


def get_formatted_name(first_name, last_name, middle_name=''):
    '''return a full name fullt formatted'''
    if middle_name:
        fullname = f'{first_name} {middle_name} {last_name}'
    else:
        fullname = f'{first_name} {last_name}'
    return fullname


name = get_formatted_name('lipson', 'kwabena', 'boateng')
print(name)
name_two = get_formatted_name('ernest'.capitalize(),
                              'ayew'.capitalize())


def squares(a, b):
    """Python code to print all the perfect
        square numbers between a and b"""
    Lists = []
    for i in range(a, b+1):
        j = 1
        while j*j <= i:
            if j*j == i:
                Lists.append(i)
            j = j+1
        i = i+1
    return Lists


print(squares(1, 500))
