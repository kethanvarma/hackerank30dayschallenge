import time

T = int(input())
for j in range(T):
    t0 = time.time()
    x = input().split()
    p_list = []
    for n in range(int(x[0]), int(x[1]) + 1):
        prime = [True for i in range(n+1)]
        i = 2
        while i*i<= n:
            if prime[i] == True:
                for k in range(i*i,n+1,i):
                    prime[k]=False
            i+=1
        if prime[-1]== True:
            p_list.append(n)

    if len(p_list) == 1:
        print(0)
    elif len(p_list) == 0:
        print(-1)
    else:
        print(p_list[-1] - p_list[0])
    print(time.time() - t0)


