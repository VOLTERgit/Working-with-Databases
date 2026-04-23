n = int(input("Enter n: "))

a, b = 0, 1
series = []

for _ in range(n+1):
    series.append(a)
    a, b = b, a + b

print(series)