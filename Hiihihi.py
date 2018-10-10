print("enter number")
x= int(input())
print("second number")
y= int(input())

if x%2==0:
     if y%2==0:
        result = x*y
        print(result)
     else:
        result= x**y
        print(result)
else:
     if y%2==0:
        result = x-y
        print(result)
     else:
        result= y+x 
        print(result)

    
