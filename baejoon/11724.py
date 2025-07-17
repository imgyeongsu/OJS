import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

n, m = map(int, input().split() )

nodes =defaultdict(list)
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    nodes[a].append(b)
    nodes[b].append(a)

visited = set()

def dfs(s):
    visited.add(s)
    for i in nodes[s]:
        if i not in visited:
            dfs(i)

n_cc = 0

for i in range(1,n+1):
    if i not in visited:
        dfs(i)
        n_cc += 1
        
print(n_cc)