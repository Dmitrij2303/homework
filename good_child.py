t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    best = 0
    for i in range(n):
        prod = 1
        for j in range(n):
            prod *= (a[j] + 1) if j == i else a[j]
        if prod > best:
            best = prod

    print(best)
