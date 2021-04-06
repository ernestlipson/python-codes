# Dictionaries
alien = {'color': 'green', 'points': 5.0}
print(type(alien))
new_points = alien['points']

print(f'you just earned {new_points} points')
# adding values to a dictionary
alien['x_position'] = 18
alien['y_position'] = 25
print(alien)

# modifying the values of a dictionary
alien['color'] = 'yellow'
print(alien)
# dictionaries can also be written as below, for readability.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print('\n{}'.format(thisdict))

# tracking the position an alien move at different levels.
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    xincrement = 1
elif alien_0['speed'] == 'medium':
    xincrement = 2
else:
    xincrement = 3

alien_0['x_position'] = alien_0['x_position'] + xincrement
print(f"\nNew position of alien is: {alien_0['x_position']}")

favlang = {
    'jen': 'python',
    'sarah': 'c ++',
    'edward': 'ruby/rass-berry',
    'philimon': 'javaScript',
    'mills': 'python',
}
print(f"Sarah's favourite language is {favlang['sarah'].title()}")
print(favlang.get('jen', 'No jen key specified'))
print('')

# looping through a dictionary
for n, l in favlang.items():
    print(f"{n.title()}'s favourite language is {l.title()}.")

# personal information
person_info = {
    'first_name': 'evans listowell',
    'last_name': 'danquah busia',
    'age': '15',
    'city': 'kwabenya',
}
print(' ')
for k, v in person_info.items():
    print(f'{k}:', v.title())
print(f'\n{person_info}')

# sample code to loop through a dict check... with a list
friends = ['phil', 'sarah', 'quansah', 'edward', 'philimon', 'jen']
for n in favlang.keys():
    print(n.title())

    if n in friends:
        lan = favlang[n].title()
        print(f"\t{n.title()}, I see you love {lan}!")

if 'erin' not in favlang.keys():
    print("\nErin, please take our poll!")
# looping through a dictionary in a sorted manner
for n in sorted(favlang.keys()):
    print(f"{n.title()}, thanks for the poll")
print('')

# looping through the values of a dictionary
print('The language of the people:')
for i in favlang.values():
    print(i.title())
print(' ')
# To see each language chosen without repetition, we can use a set
for i in set(favlang.values()):
    print(i.title())
print(' ')

river = {'nile': 'egypt', 'akosombo_dam': 'ghana', 'victoria': 'zimbabwe', }
for r, c in river.items():
    print(f'The {r.title()} runs through {c.title()}')

print('\nThe keys of the dictionary are: ')
for r in river.keys():
    print('{}'.format(r))
print('\nThe values of the dictionary are: ')
for c in river.values():
    print('{}'.format(c))

# nesting of dictionaries
'''This is called nesting. You can nest dictionaries
 inside a list, a list of items inside a dictionary, 
 or even a dictionary inside another dictionary'''
# A list of three aliens
alien_0 = {'color': 'green', 'points': 5, }
alien_1 = {'color': 'yellow', 'points': 10, }
alien_2 = {'color': 'red', 'points': 15, }

aliens = [alien_0, alien_1, alien_2]
print('\nThe dictionaries are: ')
for alien in aliens:
    print(alien)

# using range() to create a fleet of aliens:
aliens = []

for a_num in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print('...')
print(f'Total number of aliens: {len(aliens)}')
# A list in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
print(f"you ordered a {pizza['crust']} pizza"
      " with the following toppings: ")
for t in pizza['toppings']:
    print("\t" + t)
# print(pizza['toppings'])
'''You can nest a list inside a dictionary any time you want more than
    one value to be associated with a single key in a dictionary'''
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for n, l in favorite_languages.items():
    print(f"\n{n.title()}'s favourite languages are: ")
    for e in l:
        print(f"\t{e.title()}")

my_res = {
    'visual basic': {'first_sem': 'A', 'sec_sem': 'B', },
    'systems analysis': {'first_sem': 'A', 'sec_sem': 'C', },
    'numerical methods': {'first_sem': 'A', 'sec_sem': 'B', },
    'assembly lang': {'first_sem': 'B', 'sec_sem': 'C', },
    'literature': {'first_sem': 'A', 'sec_sem': 'A', },
}
for a, b in my_res.items():
    print(f"My results for {a.title()} for the year is {b.values()}")
print(f'\n{my_res.values()}')

my_res = {
    'visual basic': ['first_sem', 'A', 'sec_sem', 'B', ],
    'systems analysis': ['first_sem', 'A', 'sec_sem', 'C', ],
    'numerical methods': ['first_sem', 'A', 'sec_sem', 'B', ],
    'assembly lang': ['first_sem', 'B', 'sec_sem', 'C', ],
    'literature': ['first_sem', 'A', 'sec_sem', 'A', ],
    'electronics': ['first_sem', 'A', 'sec_sem', 'B', ],
    'Android Prog': ['first_sem', 'C', 'sec_sem', 'B', ],
    'Data base': ['first_sem', 'A', 'sec_sem', 'A', ],
}
for p, d in my_res.items():
    print(f"\n{p.title()}'s programme details is: ")
    for i in d:
        print(f"{i.title()}")
# print(type(my_res('visual basic')))
# dictionary in a dictionary
users = {
    'einstein': {
        'first': 'albert',
        'last': 'aeinstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for u, d in users.items():
    print(f"\nUsername: {u.title()}")
    print(f"\tFull name: {d['first'].title()} {d['last'].title()}")
    print(f"\tLocation: {d['location'].title()}\n")
print(users)
print(type(users['einstein']))
print(type(users))
