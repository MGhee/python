def square_of_6():
    return 6**2
result = square_of_6()
print(result)
 
from random import random

def flip_coin():
    r=random()
    if r>0.5:
        return "Heads"
    else:
        return "Tails"
print(flip_coin())

def square(num):
    return num*num
print(square(5))
print(square(2))

def number_default(num, power=2):
    return num ** power
print(number_default(2,3))
print(number_default(3))

def full_name(first="Colt" , last="Stell"):
    return "Your name is {first} {last}"
print(full_name() )

intstructor="colt"

def hello():
    return f"Hello {intstructor}"
print(hello())

total= 0

def hole():
    global total
    total +=1
    return total
print(hole())

def return_day(num):
    days=["luni","marti","miercuri", "joi","vineri","sambata","duminica"]
    if num >0 and num <= len(days):
        return days[num-1]
    return None
print(return_day(2))

l1=["mama","tata"]
l2=["mama","anca"]

def intersection(l1, l2):
    return[val for val in l1 if val in l2]
print(intersection(l1,l2))