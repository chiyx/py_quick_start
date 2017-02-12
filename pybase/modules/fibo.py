# Fibonacci numbers module

def fib(n):
    "write Finonacci series up to n"
    a, b = 0, 1
    while b < n:
        print(b, end = ' ')
        a, b = b, a + b
    print()