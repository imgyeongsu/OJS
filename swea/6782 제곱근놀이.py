T = int(input())

def is_sqrt(num):
    l = 1
    r = num//2
        
    while l<= r:
        m = (l + r) // 2
        if m * m == num:
            return True
        elif m * m <= num:
            l += 1
        elif m * m >= num:
            r -= 1
    

for _ in range(T):
    n = int(input())
    times = [0] * n+1 #times[i]는 숫자 i가 주어진 규칙하에 도달하는 가장 적은 연산 횟수이다.
    
    for i in range(2,n+1):
        times[i+1] = times[i]+1 # i+1은 기본적으로 i에 1을 더해서 만들 수 있다.
        if 