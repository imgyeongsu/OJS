x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())


def ccw(a, b, c):
    op = (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    if op > 0: return 1
    elif op < 0: return -1
    else: return 0

def intersect(a, b, c, d):
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)

    if ab == 0 and cd == 0:
        if a > b: a, b = b, a
        if c > d: c, d = d, c
        return not (b < c or d < a)  
    return ab <= 0 and cd <= 0



A = (x1, y1)
B = (x2, y2)
C = (x3, y3)
D = (x4, y4)

print(1 if intersect(A, B, C, D) else 0)
