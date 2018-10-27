class Animal:
    cool=True
    def __init__(self , name , species):
        self.name= name
        self.species= species
    def __repr__(self):
        return f"{self.name} is a {self.species}"
    def make_sound(self , sound):
        print(f"the animal says {sound}")
class Cat(Animal):
    def __init__(self, name , species , breed ,toy):
        super().__init__( name ,species="cat")
        self.breed = breed
        self.toy = toy
    def play(self):
        print(f"{self.name} plays with {self.toy}")

blue= Cat("blue" , "cat", "scottish", "string")
print(blue.play())
print(blue.species)

#d = GrumpyDict({"name":Yorik , "city":"timisoara"})
#print(d)
#d["city"]=SF
#print(d)

class GrumpyDict(dict):
    def __repr__(self):
        print("none of your bussiness")
        return super().__repr__()
    def __missing__(self , key):
        print(f"you want {key}! well there isn't one")


data = GrumpyDict({"fisrt":"tom" , "animal":"cat"})   
print(data)
data['city'] 