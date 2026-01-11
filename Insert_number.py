for _ in range(int(input())):
    a = input()[-1]
    n = list(input())
    for index in range(len(n)):
        if n[index] < a:
            n.insert(index, a)
            break
    else:
        n.append(a)
    print("".join(n))
