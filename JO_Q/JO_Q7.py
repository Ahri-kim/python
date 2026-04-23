#1314
n = int(input())

L=['A', 'B', 'C', 'D','E','F','G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
for i in range(1,n+1):
    if i%2 != 0:
        for j in range(i-1,i+n-1,1):        #0,4,8,
            if j > 26:
                j = j%26+1
            print(L[j],end=' ')
        print()
    else:
        for k in range(i*n, 2*i*n, 1):  
            if k > 26:
                k = k%26+1            #1,6,9,14
            print(L[k],end=' ')
        print()