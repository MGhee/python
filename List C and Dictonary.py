numx= [1,2,3]
y=[x*10 for x in numx]
print(y)

board=[[num for num in range(1,3)] for val in range(1,4)]
print(board)

number= dict(first=1,secon=2,third=3)
numbers={key:value**2 for key,value in number.items()}
print(numbers)

z={count:chr(count) for count in range(65,91)}
print(z)

answer={char:0 for char in 'aieou'}
print(answer)

answer=dict.fromkeys("aeiou",0)
print(answer)

person=[["name","jared"],["job","musician"],["city","Beren"]]
answer={thing[0]:thing[1]for thing in person}
print (answer)