# returning Lists and functios from a function
def person_name(fname, lname, age=None):
    """returns a dictionary"""
    person = {'firstname': fname, 'lastname': lname}
    if age:
        person['age'] = age
    return person
# the age becomes an optional positional parameter


people = person_name('Asenath', 'Noah', age=19)
print(people)
print(people['lastname'])

# using a while loop to get the user inputs


def person_name(fname, lname, age=None):
    """returns a dictionary"""
    person = {'firstname': fname, 'lastname': lname}
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print('please input your names'
          ' (press q at any point to quit)')
    first_name = input('firsname: ')
    last_name = input('lastname: ')
    if last_name or first_name == 'q':
        break

    fullname = person_name(first_name, last_name)
    print(fullname)


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")


def city_country():
    '''returns countries and cities'''
    while True:
        print('please enter the name of the country and city: ')
        print('(press q when done)')
        contry = input('input country; ')
        city = input('input city')
        if contry or city == 'q':
            break

    return f'The name of the country is {contry} with capital {city}'


print(city_country())

# passing list to functions


def greet_users(names):
    """greets people"""
    for name in names:
        msg = f'Hello {name.title()} !'
        print(msg)


usernames = ['ama', 'abebrese', 'joe wise', 'oforiwaa']
greet_users(usernames)
