from collections import deque
x, y = map(int, input().split())

def bfs(x, y):
    limit = 2 * max(x, y) + 10
    visited = [False] * limit
    queue = deque()
    queue.append((x, 0))  
    visited[x] = True

    while queue:
        loc, times = queue.popleft() #방문 시작
        if loc == y:
            return times
        for next_loc in [loc - 1, loc + 1, loc * 2]: #다음 방문
            if 0 <= next_loc < limit and not visited[next_loc]:
                visited[next_loc] = True
                queue.append((next_loc, times + 1))

print(bfs(x, y))












# 풀이 1 최적해 보장 X라는데 이유 모르겟음
x, y = map(int, (input().split()))

def nfind(x,y):
    n = 1
    while x * (2 ** n) < y:
        n += 1
    n0 = n - 1
    if x * (2 ** n) - y  > y - x * (2 ** n0):
        return n0
    else:
        return n

def walk_times(cha, n):
    result = []
    while cha != 0:
        if cha % 2 == 0:
            result.append(0)
        else:
            if cha % 4 == 1:
                result.append(1)
                cha -= 1
            else:  # n % 4 == 3 or n % 4 == -1
                result.append(-1)
                cha += 1
        cha //= 2
    for i in range(n+1,len(result)):
        if result[i] > 0:
            result[n] +=result[i] * 2 ** (i -n)
        elif result[i] < 0:
            result[n] -=abs(result[i]) * 2 ** (i -n)
    return result[:n+1]

n = nfind(x,y)
cha = y - x  * (2 ** n)

walktimes = walk_times(cha, n)
n_walks = sum([abs(w) for w in walktimes])

print(n_walks + n)

    
    

int(str(cha),32)

시그마 1~ k {ak}2^(n-k) + 2^n * x = Y
이거 맞잖아


def nfind(x,y):
    n = 1
    while x * (2 ** n) < y:
        n += 1
    n0 = n - 1
    return n, n0
#walk_times함수가 최적 해를 제시하지 못하고있음
#예를들어 x,y = 3,9 일때 [1,1] 을 반환해야하지만 [-1,2]를 반환함
def walk_times(cha, n):
    result = []
    while cha != 0:
        if cha % 2 == 0:
            result.append(0)
        else:
            if cha % 4 == 1:
                result.append(1)
                cha -= 1
            else:  # n % 4 == 3 or n % 4 == -1
                result.append(-1)
                cha += 1
        cha //= 2
    for i in range(n+1,len(result)):
        if result[i] > 0:
            result[n] +=result[i] * 2 ** (i -n)
        elif result[i] < 0:
            result[n] -=abs(result[i]) * 2 ** (i -n)
    return result[:n+1]

x, y = 3, 9
over, down = nfind(x,y)
walk_over = y - x  * (2 ** over)
walk_down = y - x  * (2 ** down)

walktimes_over = walk_times(walk_over, over)
n_walks_over = sum([abs(w) for w in walktimes_over])

walktimes_down = walk_times(walk_down, down)
n_walks_down = sum([abs(w) for w in walktimes_down])

print(min(over + n_walks_over , down + n_walks_down))
