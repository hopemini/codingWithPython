## make password using combinations
from  itertools import combinations
L, C = map(int, input().split())
array = input().split(' ')
array.sort()
vowels = ('a', 'e', 'i', 'o', 'u')

for passwd in combinations(array, L):
    count = 0
    for i in passwd:
        if i in vowels:
            count += 1
    if count >= 1 and count <= L-2:
        print(''.join(passwd))