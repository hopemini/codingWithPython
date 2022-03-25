a, b, c = map(int, input().split())

count = [0] * 10
mul = str(a * b* c)

for i in mul:
    count[int(i)] += 1

print(count)

count = [0] * 10
mul2 = a * b * c
while mul2 > 0:
    count[mul2 % 10] += 1
    mul2 //= 10
print(count)