n = int(input())

cases = [0] * (n+1)
# i) 2 X 1 로 시작하는 경우
#   n - 1 개를 배열하는 경우의 수
# ii) 1 X 2 블럭 두개로 시작하는 경우
#   n - 2 개의 타일을 배열하는 경우
if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    cases[1] = 1
    cases[2] = 2

    for i in range(3,n+1):
        cases[i] = cases[i-1] + cases[i-2]
        
        
    print(cases[n]%10007)
    
