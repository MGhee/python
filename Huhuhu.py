import platform
x= platform.system()
print(x)

import datetime
a= datetime.datetime.now()
print(a.strftime("%U"))

import json
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])

import json
x = {"cars":"Mercedes",
     "age": 23,
     "married": True,
     "kids": 2
     }

print(json.dumps(x, indent=4, separators=(";", "=")))

try:
    print(w)
except:
    print(" smth went sideways ")
finally:
    print("oops")