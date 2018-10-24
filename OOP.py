class User:
    active_users=0
    @classmethod
    def display(cls):
        print (f" There are {cls.active_users} on")
    def __init__(self , first , last , age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    def __repr__(self):
        return f"{self.first} is ...."
    def full_name(self):
        return f"{self.first} {self.last}"
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    def likes(self, thing):
        return f"{self.first} likes {thing}"

user1 = User("Anca", "Milea" , 20)
print(User.display())
user1 = User("Anca", "Milea" , 20)
print(User.display())
print(user1.likes("Ice Cream"))
print(user1.full_name())
print(user1.initials())

class Pet:
    allowed= ["cat", "rat", "snake", "tiger"]
    def __init__(self , name ,species):
        if species not in Pet.allowed:
            raise ValueError (f"You can't have a {species} pet!")
        self.name =name
        self.species =species

pet1 = Pet("Blue" , "cat")
pet2 = Pet("Bolt" , "crocodile")
print(pet1.species())


class card:
    def __init__(self , value , suit):
        self.value = value
        self.suit = suit

c= card("A", "Diamonds")
print(c.value())