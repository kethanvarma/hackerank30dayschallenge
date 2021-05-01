n = int(input())
t = n
n1=n
count = 0
while t!=0:
    t1 = t%10
    count+=1
    t = t//10
total = 0
while n1!=0:
    t2 = n1%10
    total = total+(t2**count)
    n1 = n1//10

print('True') if total==n else print('False')
