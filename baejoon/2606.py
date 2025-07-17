from collections import defaultdict
n = int(input())

node = defaultdict(list)
for _ in range(int(input())):
    com1, com2 = map(int, input().split())
    node[com1].append(com2)
    node[com2].append(com1)

for i in node:
    node[i].sort()

visit_dfs = set()

def dfs(start):
    visit_dfs.add(start)
    for i in node[start]:
        if i not in visit_dfs:
            dfs(i)

dfs(1)        
print(len(visit_dfs)-1)