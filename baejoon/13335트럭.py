n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))

from collections import deque

truck_q = deque()

for t in trucks:
    truck_q.append(t)

on_bridge = {k: None for k in range(1, w+1)}

truck_arrive = []