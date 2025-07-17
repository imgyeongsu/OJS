T = int(input())

X, N, Y, M = map(int, input().split())

# i) x와 y가 1인경우
case1 = n * m
# ii) n과 m이 1인경우
case2 = min(x, y)
# iii) x^k = y 꼴로 표현되는 경우
# ix) x=y^k 꼴로 표현되는 경우
