a = [1, 3, 6, 4, 1, 2]
n = len(a)


def getMEX(a, n):
    found = [False] * (n + 2)
    for i in range(n):
        if a[i] > 0 and a[i] <= n:
            found[a[i]] = True
    for i in range(1, n + 2):
        if found[i] == False:
            return i
    return n + 1


print(getMEX(a, n))
