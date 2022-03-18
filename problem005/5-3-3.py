n = int(input())
prod = set(map(int, input().split()))
m = int(input())
guest = list(map(int, input().split()))

for i in guest:
    if i in prod:
        print('yes', end=' ')
    else:
        print('no', end=' ')