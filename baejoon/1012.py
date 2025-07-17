import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())



for _ in range(t):
    m, n, k = map(int, input().split())
    cabbage = set()
    for _ in range(k):
        x, y = map(int, input().split())
        cabbage.add((x,y))

    visited = set()

    dx = [ -1, +1, 0, 0]
    dy = [0, 0 , +1, -1]
    def neighbors(s):
        x, y = s
        neighbors = []
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < m and 0 <= yy < n:
                neighbors.append((xx,yy))
        return neighbors
        

    def dfs(s):
        visited.add(s)
        for i in neighbors(s):
            if i not in visited and i in cabbage:
                dfs(i)
        
        
    nstart = 0
    for start in cabbage:
        if start not in visited:
            dfs(start)
            nstart += 1
    
    print(nstart)