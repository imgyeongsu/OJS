n, m = map(int, input().split())

trees = list(map(int, input().split()))

s = 0
e = max(trees)
res = 0

while s <= e :
    c = (s + e )//2
    l = sum([t - c for t in trees if t > c])
    
    if l >= m :
        res = c
        s = c + 1
    else:
        e = c - 1

print(res)