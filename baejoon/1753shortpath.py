import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

V, E = map(int, input().split())
depart = int(input())

graph = defaultdict(list)
# graph = [[] for _ in range(V+1)]

for _ in range(E):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])

cost = [float('INF')] * (V + 1)
cost[depart] = 0
prior_queue = []
heapq.heappush(prior_queue, ([0, depart]))

while prior_queue:
    now_cost, now_node = heapq.heappop(prior_queue)

    if now_cost < cost[now_node]:
        continue

    for next_node, edge_cost in graph[now_node]:
        next_cost = cost[now_node] + edge_cost
        if next_cost < cost[next_node]:
            cost[next_node] = next_cost
            heapq.heappush(prior_queue, (next_cost, next_node))


for c in cost[1:]:
    print(c if c != float('inf') else 'INF')