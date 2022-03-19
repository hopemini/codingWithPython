def search(l, h, height, m):
    while l <= h:
        mid = (l + h) // 2
        #total = 0
        #for i in height:
        #    if i > mid:
        #        total += i - mid
        total = sum([i-mid for i in height if i > mid])
        if total > m:
            l = mid + 1
        elif total < m:
            h = mid - 1
        else:
            return mid
    return l

n, m = map(int, input().split())
height = list(map(int, input().split()))
l, h = 0, max(height)

print(search(l, h, height, m))