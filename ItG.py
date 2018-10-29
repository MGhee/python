def iterator(iterable,func):
    itera = iter(iterable)
    while True:
        try:
            thing = next(itera)
        except StopIteration:
            break
        else:
            func(thing)
def square(x):
    print(x*x)

iterator("lol" , print)
iterator([1,2,3,4,5] , square)

class Counter:
    def __init__(self , low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.high:
            num= self.current
            self.current +=1
            return num
        raise StopIteration
     
for x in Counter(50,70):
    print(x)

def beat():
    nums = (1,2,3,4)
    i=0
    while True:
        if i >= len(nums) : i=0
        yield nums[i]
        i +=1


    