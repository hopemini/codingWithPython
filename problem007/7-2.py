n = int(input())

d = {}
for _ in range(n):
    student = input().split()
    d[student[0]] = int(student[1])

#print(d)
d_s = sorted(d.items(), key=lambda student:student[1])
#print(d_s)
for i in d_s:
    print(i[0], end=' ')