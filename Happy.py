class Person:
  def _init_(self, name, age):
    self.name= name
    self.age= age

  def myfunc(self):
    print("My name is " + self.name)
        
p1 = Person("Gheorghe" , 30)
p1.myfunc()

class number:
    def _iter_(self):
        self.a=1
        return self
    def _next_(self):
        x= self.a
        self.a +=1
        return x
f = number()
myiter = iter(number)
for x in myiter:
    print(x)

class number1:
    def _iter_(self):
        self.a=1
        return self
    def _next_(self):
        if self.a <=20:
         x= self.a
         self.a +=1
         return x
        else:
            raise StopIteration
f = number1()
myiter = iter(number1)
for x in myiter:
    print(x)     