N = int(input())

for _ in range(N):
    a, b, x = map(int,input().split())
    nn = 0
    while True:
        if a > b:
            b += a
            nn += 1
            if b > x:
                break
        else:
            a += b
            nn += 1
            if a > x:
                break    
        
    print(nn)
        
