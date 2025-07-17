T = int(input())

def mod(x, y, base):
    a = 1
    for _ in range(y):
        a = (a * x) % (10 ** base)
    return a

for _ in range(T):
    x, y, z = map(int, input().split())
    
    lenth = len(str(z)) + 6
    xpowy = mod(x,y, lenth)
    xpowy/z
    
    
