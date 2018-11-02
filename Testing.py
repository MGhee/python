def eat_junk(food):
     assert food in ["pizza", "shaworma", "ice_cream"] , "food must be junk food"
     return f"NOM NOM NOM I am eatin {food}"

food = input("enter a food please:")
print(eat_junk(food)) 

def add(a,b):
    """
    >>> add (2,3)
    5
    >>> add(100 ,200)
    300
    """
    return a+b

with open("novel.txt", "w") as file:
    file.write("Muahahhah")
