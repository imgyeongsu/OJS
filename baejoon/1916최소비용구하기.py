import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline

N = int(input())  # 도시 수
M = int(input())  # 버스 수

graph = defaultdict(list)
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

start_city, end_city = map(int, input().split())


costs = [float('inf')] * (N + 1)
costs[start_city] = 0
prior_queue = []
heapq.heappush(prior_queue, (0, start_city))

while prior_queue:
    now_cost, city = heapq.heappop(prior_queue)

    if costs[city] < now_cost:
        continue

    for next_city, cost in graph[city]:
        next_cost = now_cost + cost

        if next_cost < costs[next_city]:
            costs[next_city] = next_cost
            heapq.heappush(prior_queue, [next_cost, next_city])

print(costs[end_city])