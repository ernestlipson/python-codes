def chnum(xvar, yvar):
    """function that swaps two numbers"""
    xvar = xvar + yvar
    yvar = xvar - yvar
    xvar = xvar - yvar
    return xvar, yvar


newnum, oldnum = chnum(7, 19)
print(newnum, oldnum)


def chnumber(a, b):
    """function that swaps two numbers"""
    a, b = b, a
    return a, b


print(chnumber(12, 78))


# functional programming
# A key part of functional programming is higher-order functions.
# Higher-order functions take other functions as arguments
def applytwice(func, arg):
    return func(func(arg))


def addfive(x):
    return x + 5


print(applytwice(addfive, 10))


def test(func, arg):
    return func(func(arg))


def mult(x):
    return x * x


print(test(mult, 2))

# functional programming with pure functions
# the issue of writting global variables
'''The basic definition of a pure function is a function
that doesn't cause or rely on side effects.
The output of a pure function should only depend on its inputs.

There are two basic ways a function can cause side effects
that directly affect other parts of the code.
The first is by reading or writing global variables.'''

# For example:
gvalue = 0


def setvalue(x):
    global gvalue
    gvalue = x


def printvalue():
    print(gvalue)


setvalue(14)
printvalue()

'''The other way that function can create side effects
is by altering data structures.'''


# For example:
def tail(s):
    del s[0]
    return s


def print_value():
    a = [1, 2, 3]
    b = tailing(a)
    print(b)
    print(a)


print_value()

'''A pure function must not alter the value of any data structure
that is passed into it.
A pure function must not alter the value of any
data structure that is passed into it.
This version of tail is not pure.
We could create a pure version like this:'''


def tailing(s):
    return s[1:]


def print_value():
    a = [1, 2, 3]
    b = tailing(a)
    print(b)
    print(a)


print_value()


# impure functions are basically functions that
# causes a change to a given data.
def pure_function(x, y):
    temp = x + 2 * y
    return temp / (2 * x + y)


print(pure_function(12, 32))

some_list = []


def impure(arg):
    some_list.append(arg)


print(impure(12))


# named function
def polynomial(x):
    return x ** 2 + 5 * x + 4


print(polynomial(-4))

# lambda
# lambda is used to create anonymous functions
print((lambda x: x ** 2 + 5 * x + 4)(-4))
print((lambda e: e * 4 + 8)(8))


# Map And Filters
'''The built-in functions map and filter are very useful
higher-order functions that operate on lists
(or similar objects called iterables).
The function map takes a function and
an iterable as arguments,
and returns a new iterable with the function
applied to each argument.'''


def addfive(x):
    return x + 5


nums = [11, 22, 45, 58, 89]
result = list(map(addfive, nums))
print(result)

# using lambda
nums = [11, 22, 33, 44, 55, 66]
result = list(map(lambda x: x + 5, nums))
print(result)

# filters
nums2 = nums
res = list(filter(lambda x: x % 2 == 0, nums2))
print(res)


# generators
def countdown():
    icount = 5
    while icount > 0:
        yield icount
        icount -= 1


for i in countdown():
    print(i)


# Finite generators can be converted
# into lists by passing them as arguments to the list function.
def numbers(x):
    for n in range(x):
        if n % 2 == 0:
            yield n


print(list(numbers(11)))


def make_word():
    word = ""
    for ch in "spam":
        word += ch
        yield word


print(list(make_word()))

# Decorators
'''Decorators provide a way to modify functions
using other functions.
This is ideal when you need to extend
the functionality of functions that you don't want to modify.'''


def decor(func):
    def wrap():
        print("============")
        func()
        print("============")

    return wrap


def print_text():
    print("Hello world!")


decorated = decor(print_text)
decorated()

# Recursion
'''The fundamental part of recursion is self-reference -
functions calling themselves.
It is used to solve problems that can be broken up
into easier sub-problems of the same type.'''


# A classic example of a function that is implemented
# recursively is the factorial function
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print(factorial(5))
print(factorial(9))
# Recursive functions can be infinite,
# just like infinite while loops.
# These often occur when you forget to implement the base case.

'''Recursion can also be indirect.
One function can call a second, which calls the first,
which calls the second, and so on.'''


def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x - 1)


def is_odd(x):
    return not is_even(x)


print(is_odd(17))
print(is_even(23))


def fac(num):
    if num == 1:
        return 1
    else:
        return num * fac(num - 1)


print(fac(9))
