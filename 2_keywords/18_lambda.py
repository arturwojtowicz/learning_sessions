# lambda
print("----------- lambda -----------")
y = lambda x: x*x
print(y(8))

list_1 = [1,2,3,4,5,6,7,8,9]
x = filter(lambda x: x % 2 == 0, list_1)
print(x)
print(list(x))
