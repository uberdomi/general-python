# print("hello World")
import random
import math
import os
from Carro import Car

name = "Dominik"
surname = "Berez"
wholeName = name + " " + surname
print("Hey " + wholeName)
print(type(name),name)
age = 19
print(type(age),age)
print(wholeName + " " + str(age))
height = 186.6
print(height)
print(type(height))
print("Height: " + str(height))
male = True
print(type(male))
raz, dwa, trzy = True, 2, "three"
d = dd = ddd = 30
print(raz)
print(dwa)
print(trzy)
s = "witam"
print(s)
print(len(s))
print(s.find("i"))
print(s.upper())
print(s.capitalize())
print(s.count("a"))
print(s.isalpha())
print(s.isdigit())
print(s.replace("a", "o"))  # only locally
print(s.capitalize())
print(s * 4)
print((s + " ") * 4)
a = "abc"
print(a)
# print(int(a)) - only if isdigit
a = "123"
print(a)
print(int(a))
b = 2.0
print(b)
print(int(b))
b = 2.7
print(b)
print(int(b))  # round down
# state = input("how are you?") #input variables always strings
# print((state + "! nice ")*3)
# age = int(input("how old are you?"))
print(age * 2)
pi = 3.14
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
a = "raz dwa"
b = a[0:3]
print(a)
print(b)
c = a[:3:2]
print(c)
c = a[::3]
print(c)
c = a[::-1]
print(c)
d = "brrr//oookej"
slice = slice(6, -1)
print(d[slice])

# x = int(input("give number"))
x = 6
if not (x % 3 == 0 or False):
    print("nice")
elif x % 2 == 0 and True:
    print("meh")
else:
    print("not nice")
while x < 20:
    print("current: " + str(x))
    x += 1
print(x)
ee = "a"
ee = ee + "abc"
ee += "d"
# ee += None cannot concatenate None
print(ee)
for i in range(13):
    print(i)
for i in range(12, 23, 3):
    print(i)
for i in "abecede":
    print(i)
# rows = int(input("how many rows? "))
# columns = int(input("how many columns? "))
rows, columns, symbol = 6, 9, "$"
# symbol = input("symbol: ")
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
while True:
    # name = input("Enter name: ")
    if name != "":
        break
number = "123-456-7890"
for i in number:
    if i == "-":
        continue
    print(i, end="")
for i in range(1, 21):
    if i == 9:
        pass
    else:
        print(i)
food = ["pizza", "kebab", "burrito"]
print(food)
print(food[0] + " " + food[1])
aaa = [1, 2, "3"]  # lists can be of various types
print(aaa)
for x in food:
    print(x)
    food.append("pierożki")
    if len(food) > 10:
        print(food)
        food.remove("pierożki")  # only one occurrence
        print(food)
        break

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9, 0]
hehe = "adc"
# k = 42 - not iterable :(
nums = [nums1, nums2, nums3, hehe] # list
for x in nums:
    for y in x:
        print(y, end="")
    print()
student = ("dom", "berez", 21) # tuple
for x in student:
    print(x)
if "dom" in student: # contains()
    print("eureka!")
numms = {1, 2, 3, 4, 3} # set
for x in numms:
    print(x)
dic = {1: "blue", 2: "red", 3: "green"} # dictionary
print(dic[2])
print(dic.get(3))  # safu
for a, b in dic.items():
    print(a, b)


def bump():
    for i in range(10):
        print("hi")


bump()


def facc(i, j):
    if i >= 2:
        facc(i - 1, j * i)
    else:
        print(j)


def fac(i):
    facc(i, 1)


fac(6)


def facrec(i):
    if i < 2:
        return 1
    else:
        return i * facrec(i - 1)


print(facrec(6))


def hi(a, b, c):
    print(c, a, b)


hi(c="1", b="4", a="3")


def add(*args):  # args
    sum = 0
    for i in args:
        sum += i
    return sum


print(add(1, 2, 3, 4))


def hello(**kwargs):  # kwargs
    for key, value in kwargs.items():
        print("hello " + value)


hello(a="a", b="c", c="d")
print("abc{}fgh".format("ed"))
# print("abc{}fg{}h".format("ed"))
print("abc{0}fg{1}h".format("ed", ""))
# print("abc{2}fg{0}h".format("ed",""))
print("abc{1}fg{0}h".format("ed", ""))
print("abc{a}fg{b}h".format(a="ed", b=""))
print("hi {:10}!".format("Bob"))
print("hi {:>10}!".format("Bob"))
print("hi {:<10}!".format("Bob"))
print("hi {:^10}!".format("Bob"))
print("{:.2f}".format(3.1415))
x = random.randint(1, 6)
print(x)
list = ["1", "2", "3f"]
y = random.choice(list)
print(y)
with open("dupa.txt") as file:
    print(file.read())
with open('dupa.txt', 'a') as file:
    file.write(" jou")
with open("dupa.txt") as file:
    print(file.read())
car = Car(xd := "fiat", "500", 2021, "blue")
print(car.make)
print(car.model)
print(car.year)
print(car.color)
car.drive()
print(Car.wheels)
print(xd)

#foods = []
#while (food := input("what food do you like?: ")) != "quit":
  #  foods.append(food)
#print(foods)


def hello():
    print("hello")
hi = hello
hello()
hi()
say = print
say("oh ho ho")

def loud(text):
    return text.upper()
def quiet(text):
    return text.lower()
def greetings(func):
    text = func("Greetings")
    print(text)
greetings(loud)
greetings(quiet)

def divisor(x):
    def divident(y):
        return y/x
    return divident
divide = divisor(2)
print(divide(10))
age_check = lambda age: age>=18
mul = lambda x,y: x*y
print(mul(6,9))
print(age_check(20))

a = ["a", "c" , "b" , "e" , "d"]   # sort

for i in a:
    print(i)
a.sort()
for i in a:
    print(i)
a.sort(reverse=True)
for i in a:
    print(i)
b = sorted(a)
for i in b:
    print(i)

x = lambda z:z[2]
a = [('a','b','c'),('c','d','a')]
a.sort(key=x)
for i in a:
    print(i)
x = lambda z: z[1]
a.sort(key=x)
for i in a:
    print(i)

to_string = lambda x : x[0] + "-" + x[1] + "-" + x[2]  # map
b = map(to_string, a)
for i in b:
    print(i)
print(b)

a = [(0,1),(1,2),(2,3),(3,4)]   # filter
x = lambda z : z[1]%2==0
b = filter(x, a)
for i in b:
    print(i)
print(b)

import functools

letters  =["H","E",'L','L','O']
word = functools.reduce(lambda x, y: x+y, letters)   # reduce
print(word)

squares = [i*i for i in range(1,11)]
for i in squares:
    print(i)
nums = [10*i for i in range(1,11) if i>=6]
for i in nums:
    print(i)
nums = [3*i+1 if i%3!=0 else i for i in range(1,11)]
for i in nums:
    print(i)
a = {'a':312, 'b':234, 'c': 5873, 'd' : 3197, 'e' : 2137}
for i in a.items():
    print(i)
for i in a.values():
    print(i)
b = {k: v%3 for (k,v) in a.items()}
for i in b.items():
    print(i)
for i in b.values():
    print(i)
def check_temp(value):
    if value >= 70:
        return 'hot'
    elif 70 > value >= 40:
        return "warm"
    return 'cold'
cities = {'ny' : 69, 'ber' : 80, 'war' : 45, 'lon' : 51, 'bei' : 39, 'par' : 76}
print(cities)
cits = {k : check_temp(v) for (k,v) in cities.items()}
print(cits)
usernames = ['a','c','d','b'] #only as many as there are pairs
passwords = ['123','345','45654']
users = zip(usernames,passwords)
for i in users:
    print(i)
import time
print(time.ctime(0))
start = time.time()
print(time.localtime())
print(start)

import threading
print(threading.active_count())
print(threading.enumerate())

def a():
    time.sleep(0.5)
    print('a')
def b():
    time.sleep(4)
    print('b')
def c():
    time.sleep(5)
    print('c')
x = threading.Thread(target=a, args=())
x.start()
print(threading.active_count())
print(threading.enumerate())
x.join()
print(time.perf_counter())

def timer():
    print("")
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for:",count,"secs")
y = threading.Thread(target=timer, daemon=True)
# y.setDaemon(True)
y.start()

a = input("wanna end?")
print(a)
from multiprocessing import Process,cpu_count

def counter(num):
    count = 0
    while count < num:
        count += 1
    print(threading.active_count())
    print(threading.enumerate())

def main():
    a = Process(target=counter, args=(50000000,))
    a.start()
    b = Process(target=counter, args=(50000000,))
    b.start()
    a.join()
    b.join()
    print("finished in:", time.perf_counter(), 'secs')

if __name__ == '__main__':
    main()

