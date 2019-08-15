# Power/Exponents

5^3 = 5*5*5 
n^0 = 1

fractions? no
negative numbers? yes for base.  no for exponent

def power(a, b):
    if b == 0: return 1
    return a * power(a, b-1)

def iterative_exponents(base, exponent):
    product = 1
    for _ in range(b):
        product *= a
    return product

for i in range(10):
    print(f"2^{i}: {power(2, i)}")