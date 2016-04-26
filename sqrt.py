def quadratic(a,b,c):
    return (largerRoot(a,b,c), smallerRoot(a,b,c))

def largerRoot(a,b,c):
    return largerNumerator(a,b,c) / denominator(a)

def smallerRoot(a,b,c):
    return smallerNumerator(a,b,c) / denominator(a)

def largerNumerator(a,b,c):
    return -b + sqrtOfDiscriminant(a,b,c)

def smallerNumerator(a,b,c):
    return -b - sqrtOfDiscriminant(a,b,c)

def sqrtOfDiscriminant(a,b,c):
    from math import sqrt
    return sqrt((b ** 2) - (4 * a * c))

def denominator(a):
    return 2 * a
    
def main():
    a = float(input("Enter the a coefficient:"))
    b = float(input("Enter the b coefficient:"))
    c = float(input("Enter the c1 coefficient:"))
    roots = quadratic(a,b,c)
    print("The roots are", roots[0],"and", roots[1])

main()

    
