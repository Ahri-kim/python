'''
#2675
T = int(input())
E = []
for _ in range(T):
    R, S = input().split()
    r = ""
    for i in S:
        r += i * int(R)
    E.append(r)
print('\n'.join(E))

#1152
S = input().split()
print(len(S))

#2908
A, B = input().split()
a = int(A[::-1])
b = int(B[::-1])
if a > b:
    print(a)
else:
    print(b)

#2558
A = int(input())
B = int(input())
print(A + B)

#10951
import sys
for i in sys.stdin:
    A, B = map(int,i.split())
    print(A+B)

#10953
import sys
T = int(sys.stdin.readline())
S = []
for _ in range(T):
    i = sys.stdin.readline()
    A, B = i.split(',')
    S.append(int(A) + int(B))
for t in S:
    print(t)

#15740
import sys
A ,B = map(int,sys.stdin.readline().split())
print(A / B)
'''
#5622
d = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I'],
    ['J', 'K', 'L'],
    ['M', 'N', 'O'],
    ['P', 'Q', 'R', 'S'],
    ['T', 'U', 'V'],
    ['W', 'X', 'Y', 'Z']
]
w = input()
A = []
for a in w:
    found = False
    for i in range(len(d)):
        for j in range(len(d[i])):
            if d[i][j] == a:
                b = i
                c = b + 2
                A.append(c)
                found = True
                break  
        if found:
            break
print(A)