from collections import deque

n, m = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)] # 방문 배열

count_paint = 0
max_paint = 0

queue = deque()

delta_r = [1,-1,0,0]
delta_c = [0,0,1,-1]

for r in range(n):
    for c in range(m):
        # 1
        if matrix[r][c] or not visited[r][c]:
            queue.append([r,c])
            count_paint += 1
            
            visited[r][c] = True

            paint_size = 0

            # 2
            while queue:
                loc = queue.popleft()
                r, c = loc
                for i in range(4):
                    row = r + delta_r[i]
                    col = c + delta_c[i]

                    # 3
                    if 0 <= row < n and 0 <= col < m and not visited[row][col]:
                        visited[row][col] = True
                        queue.append([row, col])
                        paint_size += 1

            max_paint = max(max_paint, paint_size)
        else:
            continue

print(count_paint)
print(max_paint)




