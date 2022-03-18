n = int(input())
prod = [0] * 1000001

for i in input().split():
    prod[int(i)] = 1

m = int(input())
guest = list(map(int, input().split()))

for i in guest:
    if prod[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end= ' ')