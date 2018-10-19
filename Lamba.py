square= lambda a,b: a + b 
print(square(2,3))

nums = [1,2,3,4,5,6]

double = list(map(lambda x: x*2 , nums))
print(double)

names = ["colt", "anca", "marius" "eu"]
a_names= list(filter(lambda n: n[0]=='a', names))
print(a_names)

any([num for num in [4,2,4,5,7] if num % 2 == 0]) #?
all([num for num in [4,2,4,5,7] if num % 2 == 0]) #?

well= [ {"title":"George" , "playcount": 12},
         {"title":"Anca" , "playcount": 1},
        {"title":"EU" , "playcount": 79},
        {"title":"Mama" , "playcount": 112}
      ]
sorted(well , key= lambda w: w['playcount'])
min(well , key= lambda p: p['playcount'])

numb = [1,23,4,54,6]
max(numb)
min(numb)
numb.reverse()
print(numb)

for char in reversed("Hello mama!"):
    print(char)

abs(-123)
sum([1,2,3])
round(3.12345)

numb = [1,23,4,54,6]
nums = [1,2,3,4,5,6]
z = zip(numb,nums)

