#9312
for j in range(1, 10):
    for i in range(5, 8):
        print(f"{i} * {j} = {i*j}",end='   ')
    print()

#9323
s = int(input())
e = int(input())
for i in range(1, 10):
    if s < e:
        for j in range(s, e+1):
            print(j,'*',i,'=',i*j, end = '   ')
        print()
    else:
        for j in range(s, e-1, -1):
            print(j,'*',i,'=',i*j, end = '   ')
        print()