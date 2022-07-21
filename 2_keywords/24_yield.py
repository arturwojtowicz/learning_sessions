# yield
print("----------- yield -----------")

def even_numbers(n):
    for x in range(n):
       if (x % 2 == 0): 
           yield x

num = even_numbers(10)
print(num)
for i in num:
    print(i)

num = even_numbers(10)
print(num)
print(num.__next__())
print(num.__next__())
print(list(num))

num = even_numbers(10)
print(num)
print(num.__next__())
print(num.__next__())
print(num.__next__())
print(num.__next__())
print(num.__next__())
print(num.__next__())