V = input()
N = int(input())
from itertools import combinations as c

compositions_of_corona = []

for i in range(1, len(V) + 1):
    t1 = c(V, i)
    for k in t1:
        str1 = ''.join(k)
        compositions_of_corona.append(str1)

for i in range(N):
    Bi = input()
    print('POSITIVE') if Bi in compositions_of_corona else print('NEGATIVE')






