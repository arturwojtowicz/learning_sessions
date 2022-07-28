# We have list of 100 numbers - [0, 1, 2, 3, 4, 5, 6, ..., 97, 98, 99, 100]
# If the number is divisible by 3 then print Fizz
# If the number is divisible by 5 then print Buzz
# If the number is divisible by both 3 and 5 print FizzBuzz
# Otherwise just print the number
# Checking is value divisible in python, You can use modulo f.e. check if value is divisible by 2 ->  x % 2 == 0


def foo_bar(n: list):
    for num in n:
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def run(x):
    if isinstance(x, list):
        foo_bar(x)
    else:
        print("Ooopsie")

run(list(range(1, 151)))
run("Hehe")
