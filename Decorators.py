def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!!")
        fn()
        print("Have a great day!!")
        return wrapper

@be_polite
def greet():
    print("My name is Colt!")

@be_polite
def rage():
    print("I hate you!!")

#greet()
#rage()
from functools import wraps
def log(fn):
    @wraps(fn)
    def wrapper(*args, **kargs):
        print (f"you are about to call {fn.__name__}")
        print (f"you are about to call {fn.__doc__}")
        return fn(*args , **kargs)
    return wrapper

@log
def add(x,y):
    return x+y

print(add.__doc__)


