import math

def odd_series(n):
    s = 0
    for i in range(1, n+1, 2):
        s += (i**2) / math.factorial(i)
    return s

def even_series(n):
    s = 0
    for i in range(2, n+1, 2):
        s += (i**2) / math.factorial(i)
    return s

n = int(input("Enter n: "))
print("Odd series:", odd_series(n))
print("Even series:", even_series(n))