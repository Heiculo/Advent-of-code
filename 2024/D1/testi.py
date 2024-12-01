from collections import Counter

A = [2, 3, 5,6,9]
B = [1,3,3,0,9]

i = 0
Summa = 0
print(Counter(B))
for num in A:
    if num in B:
        Summa += num*B[num]

print(Summa)
