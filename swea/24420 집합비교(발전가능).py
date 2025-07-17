N = int(input())
for _ in range(N):
    NA, NB = map(int, input().split())
    A = set(list(map(int, input().split())))
    B = set(list(map(int, input().split())))
    
    if A < B:
        print('<')
    elif A > B:
        print(">")
    elif A == B:
        print('=')
    else:
        print('?')
    
    