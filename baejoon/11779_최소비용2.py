

# import sys
# from collections import defaultdict
# import heapq

# input = sys.stdin.readline


# n = int(input()) # 도시의 수
# m = int(input()) # 버스의 수

# graph = defaultdict(list)

# for _ in range(m):
#     s, e, c = map(int, input().split()) # s:출발 , e:도착, c:비용
#     # print(s, e, c)
#     graph[s].append((e,c))
#     print(graph) # 이부분을 살리고 죽이고가 왜 입력할때 차이가 나는가

# start, end = map(int, input().split())
# print(start)

# #경로를 저장하는 리스트를 만들어야함
# #어떻게 만들까? 모든 도착 지점에 대해서 만들어? #일단 모든 도착지점에 대해서 만들고 그 다음 필요한것만 만드는 방법으로

# bus_path = [[start] for _ in range(n+1)] # bus_path[i] : 출발지에서 i번 도시까지 가는데 최소비용 경로를 저장할 리스트


# # 초기 경로 초기화 
# cost = [float('inf')] * (n + 1)
# cost[start] = 0 # 시작 도시의 비용은 0

# # 우선순위 큐 선언
# prior_queue = []
# heapq.heappush(prior_queue, (0, start)) # 초기 비용, 시작 위치 push

# while prior_queue:
#     current_cost, current_loc = heapq.heappop(prior_queue)

#     if current_cost > cost[current_loc]:
#         continue

#     for next_loc, edge_cost in graph[current_loc]:
#         next_cost = cost[current_loc] + edge_cost

#         # 다음 위치의 최소 비용이 갱신되었을때
#         if next_cost <= cost[next_loc]:
#             cost[next_loc] = next_cost
#             heapq.heappush(prior_queue, (next_cost, next_loc))
#             # 다음 위치의 최적 경로는 현재 위치의 최적 경로에 다음 위치를 더함으로서 만든다
#             bus_path[next_loc] = bus_path[current_loc] + [next_loc] # bus_path는 이 코드로 인해 항상 최적의 경로를 저장하고 있는가?

# # 입력값에 스타트를 바꿔도 왜 1로 저장되는가
# # print(n, m, start)
# # print(graph)

# print(len(bus_path[end]))
# print(cost[end])
# print(*bus_path[end])



import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline


n = int(input()) # 도시의 수
m = int(input()) # 버스의 수

graph = defaultdict(list)

for _ in range(m):
    s, e, c = map(int, input().split()) # s:출발 , e:도착, c:비용
    graph[s].append((e,c))

start, end = map(int, input().split())



bus_path = [[start] for _ in range(n+1)] # bus_path[i] : 출발지에서 i번 도시까지 가는데 최소비용 경로를 저장할 리스트


# 초기 경로 초기화 (아주 큰 수로)
cost = [float('inf')] * (n + 1)
cost[start] = 0 

# 우선순위 큐 선언
prior_queue = []
heapq.heappush(prior_queue, (0, start)) # 초기 비용, 시작 위치 push

while prior_queue:
    current_cost, current_loc = heapq.heappop(prior_queue)

    if current_cost > cost[current_loc]:
        continue

    for next_loc, edge_cost in graph[current_loc]:
        next_cost = cost[current_loc] + edge_cost

        if next_cost < cost[next_loc]:
            cost[next_loc] = next_cost
            heapq.heappush(prior_queue, (next_cost, next_loc))
            bus_path[next_loc] = bus_path[current_loc] + [next_loc]


print(cost[end])
print(len(bus_path[end]))
print(*bus_path[end])
