import sys
from collections import deque

r, c = map(int, input().split())

mmap = [] 
for ri in range(r):
    rows = list(map(int, sys.stdin.readline().split()))
    mmap.append(rows)
    for ci in range(c):
        if rows[ci] == 2:
            start = (ri, ci)


queue = deque()
queue.append((start, 0))

visited = [[False] * c for _ in range(r)]
time_array = [[-1] * c for _ in range(r)]

visited[start[0]][start[1]] = True
time_array[start[0]][start[1]] = 0
while queue:
    loc, times = queue.popleft()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        x, y = loc
        if (0 <= x + dx[i] < r) and (0 <= y + dy[i] < c) and mmap[x + dx[i]][y + dy[i]] == 1 and not visited[x+dx[i]][ y+dy[i]]:
            queue.append(((x+dx[i], y+dy[i]), times +1))
            visited[x+dx[i]][y+dy[i]] = True
            time_array[x+dx[i]][y+dy[i]] = times + 1
            

for i in range(r):
    for j in range(c):
        if mmap[i][j] == 0:
            print(0, end=' ')
        else:
            print(time_array[i][j], end=' ')
    print()