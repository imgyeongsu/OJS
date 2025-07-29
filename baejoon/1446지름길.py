

n, d = map(int, input().split())

shortcuts = [list(map(int, input().split())) for _ in range(n)] #(출발, 도착, 비용)



################## DP 관점 ######################
starts = [info[0] for info in shortcuts]
ends = [info[1] for info in shortcuts]
costs = [info[2] for info in shortcuts]
# shortcut_dict = {end: [start, cost] for start, end, cost in shortcuts}


cost = [0] * (d+1)
current_loc = 0

while current_loc < 150:
    cost[current_loc + 1] = cost[current_loc] + 1
    if current_loc+1 in ends:
       
        idxs = list(filter(lambda x: ends[x]==current_loc+1, range(len(ends)))) #도착지가 같은 모든 idx에 대해서
        min_cost = float('inf')
        for idx in idxs: #도착지가 같은 모든 지름길 idx를 순회한다.
            # print(starts[idx])
            if cost[starts[idx]] + costs[idx] < min_cost: # 거길 도착하는 가장 작은 비용값 계산
                min_cost = cost[starts[idx]] + costs[idx]
        if cost[current_loc+1] > min_cost: # 그 비용이 지름길 이용x 보다 저렴하다면
            cost[current_loc+1] = min_cost # 교체

    current_loc +=1

print(cost[d])

