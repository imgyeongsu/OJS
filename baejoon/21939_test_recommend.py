# 문제 힙 : (문제 난이도, 문제 번호)
import heapq

N = int(input()) # 문제 갯수

problem_max_heap = []
problem_min_heap = []
problem_valid = dict() # 어떡하지? 문제 번호 : True, False

# 데이터 입력

for _ in range(N):
    p_number, difficult = map(int, input().split())
    heapq.heappush(problem_max_heap, (-difficult, -p_number)) # 최대 힙
    heapq.heappush(problem_min_heap, (difficult, p_number)) # 최소 힙
    problem_valid[(p_number,difficult)] = True

M = int(input()) # 명령어 갯수

for _ in range(M):
    query = input()
    split_query = query.split()
    if len(split_query) == 3:
        cmd, p_number, difficult = split_query
        p_number = int(p_number)
        difficult = int(difficult)
    else:
        cmd, val = split_query

    if cmd == 'recommend':

        if val == '1':
            while problem_max_heap:
                difficult, p_number = problem_max_heap[0]
                p_number = -p_number
                if problem_valid.get((p_number, -difficult), False):
                    print(p_number)
                    break
                heapq.heappop(problem_max_heap)
        else:
            while problem_min_heap:
                difficult, p_number = problem_min_heap[0]
                if problem_valid.get((p_number, difficult) , False):
                    print(p_number)
                    break
                heapq.heappop(problem_min_heap)

    elif cmd == 'add':
        heapq.heappush(problem_max_heap, (-difficult, -p_number))  # 최대 힙
        heapq.heappush(problem_min_heap, (difficult, p_number))  # 최소 힙
        problem_valid[(p_number,difficult)] = True


    else:  # solved P

        target_p = int(val)

        for k in problem_valid:

            if k[0] == target_p:
                problem_valid[k] = False



