import array
import array as a
import math as k

alien_0 = {'color': 'green'}

print(alien_0['color'])

work = {'work': 'using', 'points': '19'}
new = work['points']
off = work['work']

print('A printing work earned {}'.format(new+' points'))
print(alien_0)

work['x_position'] = 5.9
work['y_position'] = 56
print(work)

Settings = {'color': 'red', 'points': 98}

print(Settings)
Settings['color'] = 'green'
print(f"the color is now {Settings['color']}")

print(2 == 2)
print(5 != 5)
print(6 < 8 < 9)
print('h' == 'h' and 2 == 2)
print(not(1 == 1))

hungry = True
if hungry:
    print('it is true')
    pass

my_list = [1, 4, 6, 3, 2, 1, 8, 9, 6, 5, 4, 2, 1]
list_sum = 0
for num in my_list:
    list_sum = list_sum + num

print(list_sum)
print(sum(my_list))

mystring = 'sammy'
for letter in mystring:
    if letter == 'a':
        break
    print(letter)
print(mystring[1])

print('after many days')
# Arrays in python
# arrays in python are of no specific size
vals = a.array('i', [1, 3, 7, 9, 13])  # creating an array of int
print(vals)
print(vals.buffer_info())  # returns the address and size of the
# array
vals.reverse()  # reverses the given array
print(vals)
# printing items in a list
for i in vals:
    print(i)
print(vals[2])
# while loop to print array elements
count = 0
while i < len(vals):
    print(vals[i])
    # count += 1
    i += 1
    # break
# creating a new array from an existing array
newArr = a.array(vals.typecode, (a for a in vals))
print(list(newArr))
# sqauring or modifying new array b4 creating
newArr = a.array(vals.typecode, (a * a for a in vals))
print(list(newArr))

# taking user input into an array
arrayA = a.array('i', [])
user = int(input('please input the length of the array: '))
for i in range(user):
    xuser = int(input('please enter the values of the array: '))
    arrayA.append(xuser)

print(arrayA)
# verifying if an element is found in array
val = int(input('enter the value for search: '))
for k in arrayA:
    if k == val:
        print(k, 'is in Array')
        break
else:
    print('value was not found')

# verifying and showing the index of the element
n = 0
for e in arrayA:
    if e == val:
        print(n)
        break
    k += 1
# using buit-in-fxn
print(arrayA.index(val))


newarray = array.array('i', [12, 67, 23, 56])
print(newarray)
print(newarray[1])


print(k.sqrt(18))
print(bin(25))
print(0b1110001)

xnum = input('input num: ')
anum = int(xnum)
ynum = input('input num-2: ')
bnum = int(ynum)
znum = anum + bnum
print(znum)

# however the above lines of code can be modified.
xnum = int(input('enter num A: '))
ynum = int(input('enter num B: '))
znum = ynum + xnum
print(znum)

i = 1
while i <= 5:
    print('*', end='')
    j = 1
    while j <= 5:
        print('*', end='')
        j = j + 1

    i = i + 1
    print()

a_list = [3, 5, 6, 8]
for i in a_list:
    print(i)
    print(i - 1)
