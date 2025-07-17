from collections import deque
c, r = map(int, input().split())

arr = []
welldone = []

for ri in range(r):
    rows = list(map(int, input().split()))
    arr.append(rows)
    for ci in range(c):
        if rows[ci] == 1:
            welldone.append((ri,ci))
    
queue = deque()


queue.extend(welldone)
visited = [[False] * c for _ in range(r)]
days = [[0] * c for _ in range(r)]

for x, y in welldone:
    visited[x][y] = True

dx = [-1,1,0,0]
dy = [0,0,-1,1]


while queue:
    loc = queue.popleft()
    x, y = loc
    for i in range(4):
        nx = x +dx[i]
        ny = y +dy[i]
            
        if 0<= nx < r and 0 <= ny < c and not visited[nx][ny]:
            if arr[nx][ny] == 0 :
                visited[nx][ny] = True
                days[nx][ny] = days[x][y] + 1
                queue.append((nx,ny))


max_day = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == 0 and not visited[i][j]:
            print(-1)
            exit()
        max_day = max(max_day, days[i][j])

print(max_day)

