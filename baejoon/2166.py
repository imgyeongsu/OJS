import sys

n = int(input())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ans = 0
for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i+1) % n]
    ans += (x1 * y2 - x2 * y1)

print(f"{abs(ans)/2:.1f}")