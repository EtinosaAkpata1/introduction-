a = [1,2,3,4]
b = [1,2,3,4]
c = a
print("id pf a is ", id(a))
print("id of b is", id(b))
print("id of b is", id(c))
print(a is b)
print(a is c)
print(b is c)
print(a is not b)
print( a is not c)