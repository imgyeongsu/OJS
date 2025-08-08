# 최소힙 최대힙
# 있는지 없는지 관리


import heapq

T = int(input())

for _ in range(T):

    k = int(input())
    min_heap = []
    max_heap = []
    visited = dict()



    for i in range(k):
        cmd, val = input().split()
        val = int(val)

        if cmd == 'I':
            heapq.heappush(min_heap, (val, i))
            heapq.heappush(max_heap, (-val, i))
            visited[i] = True

        elif cmd == 'D':
            if val == 1: # 최대값 삭제
                while max_heap and not visited.get(max_heap[0][1], False):
                    # max_heap에 원소가 없거나
                    # max_heap[0][1] = 최댓값의 id
                    # 를 조회했을때 없으면(값이 False) 반복 종료

                    # min_heap에서 방출을 해서 날려버렸을 경우에 대해
                    heapq.heappop(max_heap) #
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            elif val == -1:
                while min_heap and not visited.get(min_heap[0][1], False):
                    heapq.heappop(min_heap) 
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
        
    while max_heap and not visited.get(max_heap[0][1], False):
        heapq.heappop(max_heap)
    while min_heap and not visited.get(min_heap[0][1], False):
        heapq.heappop(min_heap)

    if not min_heap or not max_heap:
        print('EMPTY')
    else:
        print(-max_heap[0][0], min_heap[0][0])
