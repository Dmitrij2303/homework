n = int(input())
a = list(map(int, input().split()))

if all(x == 0 for x in a):
    print("NO")
else:
    s = sum(a)
    print("YES")
    if s != 0:
        print(1)
        print(1, n)
    else:
        i = next(idx for idx, x in enumerate(a, start=1) if x != 0)
        print(2)
        print(1, i)
        print(i + 1, n)
