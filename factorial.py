# Factorial

6! = 6 * 5 * 4 * 3 * 2 * 1 = 720
4! = 4 * 3 * 2 * 1 = 24

what about 0? 0
what about negatives? none allowed
integer only

def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)

def factorial_iterative(n):
    product = 1
    for num in range(1, n + 1):
        product *= num
    return product

for i in range(10):
    print(f"{i}: {factorial(i)}")