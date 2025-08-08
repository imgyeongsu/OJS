from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

arrive, M = map(int, input().split())

# 1
graph = defaultdict(list)
for _ in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])
    graph[end].append([start, cost])

# 2
cow = [float('inf')] * (arrive + 1)
cow[1] = 0
prior_queue = []
heapq.heappush(prior_queue, (0, 1))

# 3
while prior_queue:
    current_cow, current_loc = heapq.heappop(prior_queue) # 큐에서 현재 만난 소의 수와 위치를 반환
    
    # 4
    if current_cow > cow[current_loc]: # 현재 소와 위치의 소를 비교해서 현재 소가 더 크면 다음 단계로 갈 가치가 없다 바로 넘어가
        continue
    
    # 5
    for meet_cow, next_loc in graph[current_loc]: # 현재 위치에서 다음 위치와 

        next_cow = current_cow + meet_cow

        # 6
        if next_cow < cow[next_loc]:
            cow[next_loc] = next_cow
            heapq.heappush(prior_queue, (next_cow, next_loc))

print(cow[arrive])
