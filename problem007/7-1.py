n = int(input())
L = []
for _ in range(n):
    L.append(int(input()))

#L = sorted(L, reverse=True)
L.sort(reverse=True)
for i in L:
    print(i, end=' ')