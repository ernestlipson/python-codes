from itertools import accumulate, takewhile
import itertools as it

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))


def mathsfxn(a, b):
    return a + b


# mathsfxn(4,6,7)


squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[0:])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

# List slices can also have a third number, representing the step, to include only alternate values in the slice.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])
print(squares[::4])

# Negative values can be used in list slicing
# (and normal list indexing). When negative values
# are used for the first and second values in a slice
# (or a normal index), they count from the end of the list.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])
print(squares[::-1])
print(squares[7:5:-1])

# list comprehension. A list can be formed by using a code
nums = [i * 2 for i in range(10)]
print(nums)

evens = [i ** 2 for i in range(10) if i ** 2 % 2 == 0]
print(evens)

evens = [i ** 2 for i in range(10)]
print(evens)

odds = [i ** 2 for i in range(10 * 100)]
print(odds)


# even = [2*i for i in range(10**100)]
# print(even)


def listitems(lista, listb):
    for i in lista:
        listb.append(i)


office = [2 ** 3 for i in range(100)]
items = ['many', 'names', 78.99, 'africa']

print(listitems(office, items))

# sets
newset = {19, 6, 17, 8, 6, 2, 5}
print(newset)

'''some characteristics of sets:
They are unordered, which means that they can't be indexed.
They cannot contain duplicate elements.
Due to the way they're stored, it's faster to check whether
an item is part of a set, rather than part of a list.'''
nums = {1, 7, 34, 16, 19}
(nums.add(-14))
(nums.remove(7))
print(nums)
# Basic uses of sets include membership testing
# and the elimination of duplicate entries.
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)  # combine items in either first or second
print(first & second)  # combine items in both first and second
print(first - second)  # gets item in first only and not second
print(second - first)  # gets item in second only and not first
print(first ^ second)  # gets items in either sets uniquely and + them

# itertools
'''The module itertools is a standard library
that contains several functions that are useful
in functional programming.
One type of function it produces is infinite iterators.
The function count counts up infinitely from a value.
The function cycle infinitely iterates through
an iterable (for instance a list or string).
The function repeat repeats an object,
either infinitely or a specific number of times. '''

for e in it.count(6, 2):
    print(e)
    if e >= 11:
        break

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))

nums = [4, 7, 8]
message = 'Numbers: {0} {1} {2}'.format(nums[0], nums[1], nums[2])
print(message)
'''Each argument of the format function is placed
in the string at the corresponding position,
which is determined using the curly braces { }.'''

print("{0}{1}{0}".format("abra", "cad"))

# stirng formatting can also be done with named arguments
a = '{x},{y}'.format(x=5, y=12)
print(a)

# string functions
name = 'ernest'
lname = 'lipson'
# fullname = name.join([lname])
print(name, ', '.join(['kofi adomah']))
print('kofi adomah'.replace('adomah', 'darko'))
print('This is a sentence'.startswith('This'))
print('This is a sentence'.endswith('sentence'))
print('Mongoly a new kind of programming'.split())
print('calories'.upper())

# Numeric fxns
'''To find the maximum or minimum of some numbers or a list,
you can use max or min.
To find the distance of a number from zero (its absolute value),
use abs.
To round a number to a certain number of decimal places, use round.
To find the total of a list, use sum.'''

print(abs(-99.87))
nsum = sum([14, 56, 78, 99, 12, 45])
print(nsum)

# list functions
nums = [55, 44, 33, 22, 11]
if all([i >= 5 for i in nums]):
    print('all numbers are greater than 5')

if any([i % 2 == 0 for i in nums]):
    print('at least one is even')
# The function enumerate can be used to iterate
# through the values and indices of a list simultaneously.
for e in enumerate(nums):
    print(e)


# files, reading files
# program shows a function that counts how many times
# a character occurs in a string.


def countchar(atext, char):
    count = 0
    for c in atext:
        if c == char:
            count += 1
        return count


print(countchar('Many schools are opening', 'are'))

'''This function takes as its arguments the text of the
file and one character, returning the number
of times that character appears in the text.'''

filename = input("Enter a filename: ")
with open(filename) as f:
    text = f.read()

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))
