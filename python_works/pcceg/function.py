def app_design(afunction, bcompleted):
    """docstring: function that prints design
       and moves List items from the original
       to the other. Arguments passed must be a
       List and one empty list"""
    while afunction[:]:
        my_function = afunction.pop()
        print(f'printing design: {my_function}')
        bcompleted.append(my_function)

    return bcompleted


model = [6, 89, 99, 34, 21, 56]
pendant = []

app_design(model, pendant)
print(pendant)
print(' ')
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print('\n{}'.format(completed_models))

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


def print_models(xunprinted_designs, xcompleted_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while xunprinted_designs:
        adesign = xunprinted_designs.pop()
        print(f"Printing model: {adesign}")
        xcompleted_models.append(adesign)


def show_completed_models(complete_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")

    for complete in complete_models:
        print('\t{}'.format(complete_models))


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

design = ['shirt', 'trouser', 'nicka']
models = []
print(' ')
print_models(design, models)
show_completed_models(models)

design = ['shirt', 'trouser', 'nicka']
print(design)
design.append('skirt')
print(design)

# preventing functions from making changes to a list
function = ['apple X', 'samsung J3', 'nokia 360', '3310']
completed = []
print(app_design(function[:], bcompleted=completed))
print(function)


# creating an arbitrary no for arguments fxns
def pizza(*topping):
    """pizza"""
    print('available topping(s) are: ')
    for top in topping:
        print(f'- {top}')

    return topping


pizza('jk', 'tl', 'py', 'df')
pizza('pepperoni')
pizza('mushrooms', 'green peppers', 'extra cheese')
print(pizza('mushrooms', 'green peppers', 'extra cheese'))


# mixing positional and abitrary
"""Python matches positional and keyword arguments first
and then collects any remaining arguments in the final
parameter."""


def make_pizza(size, *args):
    """gives pizza details"""
    print(f'\nmaking a {size}-inch pizza with the following'
          ' toppings: ')
    for t in args:
        print(f' -{t}')


# the generic parameter name for arbitrary arguments is *args


make_pizza(23, 'mua', 'mushroom', 'chicken')


# arbitrary keyword arguments


def build_profile(fname, lname, **kwargs):
    """building a dictionary profile of a person"""
    kwargs['first name'] = fname.capitalize()
    kwargs['last name'] = lname.capitalize()

    return kwargs


person = build_profile('ernest', 'darko', field='chemistry',
                       location='princeton', hobby='soccer')
print(person)
# parameter name **kwargs is used
# to collect non-specific keyword arguments
