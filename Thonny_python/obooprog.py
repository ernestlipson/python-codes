# classes
class Cat:
    def __init__(self, color, leg):
        self.color = color
        self.leg = leg


felix = Cat('ginger', 18)
print(felix.color)
print('')


class Dog:
    color = 'pink-brown'

    def __init__(self, nam, color, sound):
        self.nam = nam
        self.color = color
        self.sound = sound

    def bark(self):
        self.sound = 'wo wo wo'
        print(self.sound)


dog = Dog('puppy', 'red', 'miawwww')
print(dog.sound)
dog.bark()
print(dog.color)
print(Dog.color)
'''class attributes are shared by all instances of a class'''


# inheritance
class Animal:
    def __init__(self, nam, size):
        self.nam = nam
        self.size = size


def cat():
    print('python prog')


class Cat(Animal):
    pass


def bark():
    print('woof')


class Dog(Animal):
    pass


fido = Dog('joghn', 12)
print(fido.nam)


class A:
    def method(self):
        print(1)


class B(A):
    def method(self):
        print(2)


B().method()
'''If a class inherits from another with the same
attributes or methods, it overrides them.'''


# magic methods
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


vector_one = Vector(12, 13)
vector_two = Vector(13, 67)
result = vector_one + vector_two
print(result.x, result.y)
'''The __add__ method allows for the definition
of a custom behavior for the + operator in our class.
As you can see, it adds the corresponding attributes of
the objects and returns a new object, containing the result.
Once it's defined, we can add two objects of the class together.'''


class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])


spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)


# Data Hiding
class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

    @property
    def hiddenlist(self):
        return self._hiddenlist


queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue.hiddenlist)


class Spam:
    __egg = 7

    def __init__(self):
        self.__egg = None
        self._Spam__egg = None

    def print_egg(self):
        print(self.__egg)

    @property
    def Spam__egg(self):
        return self._Spam__egg


s = Spam()
s.print_egg()
print(s.Spam__egg)
print(s.__egg)


# class methods
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)


square = Rectangle.new_square(5)
print(square.calculate_area())
'''new_square is a class method and is called on the class,
rather than on an instance of the class.
It returns a new object of the class cls.
Technically, the parameters self and cls are just conventions;
they could be changed to anything else.
However, they are universally followed,
so it is wise to stick to using them.'''


# static methods
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True


ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validate_topping(i) for i in ingredients):
    pizza = Pizza(ingredients)


# properties
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True


# properties continuation
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Sw0rdf1sh!":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")


pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)