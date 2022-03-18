def search(prod, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if prod[mid] == target:
            return mid
        elif prod[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

n = int(input())
prod = list(map(int, input().split()))
prod.sort()

m = int(input())
guest = list(map(int, input().split()))

for i in guest:
    result = search(prod, i, 0, n-1)
    if result != -1:
        print('yes', end=' ')
    else:
        print('no', end=' ')