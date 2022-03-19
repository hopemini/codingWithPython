from bisect import bisect_left, bisect_right

n = int(input())
prod = list(map(int, input().split()))
prod.sort()

m = int(input())
guest = list(map(int, input().split()))

for i in guest:
    l = bisect_left(prod, i, 0, n-1)
    #r = bisect_right(prod, i, 0, n-1)
    #print(l, r)
    if l != len(prod) and i == prod[l]:
        print('yes', end=' ')
    else:
        print('no', end=' ')
