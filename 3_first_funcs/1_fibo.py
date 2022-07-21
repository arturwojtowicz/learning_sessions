# Live programming - Fibonacci sequence
# Fibonacci(0) == [0]
# Fibonacci(1) == [0, 1]
# Fibonacci(2) == [0, 1, 1]
# Fibonacci(3) == [0, 1, 1, 2]
# Fibonacci(4) == [0, 1, 1, 2, 3]
# Fibonacci(5) == [0, 1, 1, 2, 3, 5]
# Fibonacci(6) == [0, 1, 1, 2, 3, 5, 8]
# Fibonacci(7) == [0, 1, 1, 2, 3, 5, 8, 13]
# Fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13, 21]
# Fibonacci(9) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# Fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def fibo(n: int) -> int: ...


from datetime import datetime, timedelta

for i in range(35):
    time_now = datetime.now()
    print(i, fibo(i))
    time_delta = datetime.now() - time_now
    print(time_delta)


time_now = datetime.now()
print([fibo(i) for i in range(35)])
time_delta = datetime.now() - time_now
print(time_delta)
