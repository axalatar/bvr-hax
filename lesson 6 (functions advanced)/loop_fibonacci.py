def fibonacci_loop(n):
    b, a = 0, 1
    for i in range(n):
        b, a = a, a + b
    return b
print(fibonacci_loop(100))