n, m = map(int, input().split())
L = []
T = 0
C = 0
for i in range(n):
    L.append(list(map(int, input().split())))
while True:
    for i in range(n):
        for j in range(m):
            if L[i][j] == -1:
                L[i][j] = 0
    s = [(0, 0)]
    L[0][0] = -1
    while s:
        x, y = s.pop()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if L[nx][ny] == 0:
                    L[nx][ny] = -1
                    s.append((nx, ny))
    melt = []
    count = 0
    for i in range(n):
        for j in range(m):
            if L[i][j] == 1:
                count += 1
                air = 0
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if L[nx][ny] == -1:
                            air += 1
                if air >= 2:
                    melt.append((i,j))
    if not melt:
        C = count
        break
    for x, y in melt:
        L[x][y] = 0
    T += 1
print(T)
print(C)