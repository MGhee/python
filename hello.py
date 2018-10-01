x=2
print(x)
a= "Hello, World"
print(a.upper())
print(len(a))
y=1
print(x+y)
x= "Mama is"
print("Mama is " + x)
print(x.lower())
print(type(y))
print(float(y))

x=5
x+=3
print(x)
print(x!=y)
print(x<y)
print(not(x>2 and x<10))
print(x<2 or x>1)
x= "Mama"
print("Mama" in x)
x=5
y=5
if x>y:
    print("x is greater than y ")
elif x == y:
    print("x is equel with y ")
else:
    print("y is greater than x ")

x=4
y=3
if x>y or x<y: 
    print("one of them is true ")
print("Mama") if x>y else print("super")
i=2
while i<6:
    print(i)
    i+=1
i=2    
while i<6:
    print(i)
    if i == 3:
        break
    i+=1

for x in "Mama":
    print(x)
bama= ["Mama", "Tata", "Anca"]
for x in bama:
    print(x)
    
fruits= ["Canana" , "Pamama", "Banana"]
for x in fruits:
    if x == "Banana":
        break
    print(x)
for x in range(2,12,5):
    print(x)
else:
    print("Got it ")
    
fruits= ["Canana" , "Pamama", "Banana"]   
bruits= ["Big" , "Small", "Aha"]   
for x in fruits:
    for y in bruits:
        print(x,y)    
def f(k):
  if(k>0):
    result = k+f(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
f(6)

list = ["banana", "apple", "biscuit"]
list.insert(1,"orange")
list.remove("apple")
list.append("sugar")
list.extend("banana")
list.count("banana")
print(list)

tuple = ("banana", "apple", "biscuit", "apple")
tuple.count("apple")
print(tuple)

set = {"banana", "apple", "biscuit", "apple"}
set.update(["mama", "sugar"])
set.discard("mama")  
for x in set:
    print(x)

dict = {
    "brand": "Ibiza",
    "year": 1932,
    "motor": "v6"
}
dict["colort"]= "blue"
del dict["year"]
x = dict.values()
x= dict.get("motor")
print(dict)
print(x)
def f(k):
     print(k + " Milea")
f("Anca")
f("Gheorghe")

def f(nat = "romanian"):
    print("I am an " + nat)
f("englishman")
f("irish")
f()

def f(x):
    return 10-x
print(f(2))
print(f(9))
print(f(5))
x= lambda a, b, c : a+b+c
print(x(2,3,1))
def f(n):
    return lambda a: a*n
my3 = f(2)
my2 = f(3)
print(my3(11))
print(my2(11))

cars = ["Volvo", "Toyota", "Mercedes"]
cars.append("Ibiza")
cars[2]= "Worls"
print(cars)

      
