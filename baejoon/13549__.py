from collections import deque
x, y = map(int, input().split())

def bfs(x, y):
    limit = 2 * max(x, y) + 10
    visited = [False] * limit
    queue = deque()
    queue.append((x, 0))  
    visited[x] = True

    while queue:
        loc, times = queue.popleft() #방문 시작
        if loc == y:
            return times
        move = [loc - 1, loc + 1, loc * 2]
        for i in range(3): #다음 방문
            next_loc = move[i]              
            if 0 <= next_loc < limit and not visited[next_loc]:
                visited[next_loc] = True
                if i in [0,1]:
                    queue.append((next_loc, times + 1))
                else:
                    queue.append((next_loc, times))

print(bfs(x, y))

이렇게 풀면 안될거같음 먼저 도착하니까 time을 냅다 집어넣으면 되는데 이건 뒤에 도착해도 time이 더 낮을수 잇음
