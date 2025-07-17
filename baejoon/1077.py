n, m = map(int, input().split())

n_vertex = []
m_vertex = []

for _ in range(n):
    vertex = list(map(int, input().split()))
    n_vertex.append(vertex)

for _ in range(m):
    vertex = list(map(int, input().split()))
    m_vertex.append(vertex)

    
### spyder 데이터입력
data = '''6 4
-2 0
-1 -2
1 -2
2 0
1 2
-1 2
0 -3
1 -1
2 2
-1 0'''.split('\n')

n, m = map(int, data[0].split())

n_vertex = []
m_vertex = []
for i in range(n):
    vertex = list(map(int, data[i+1].split()))
    n_vertex.append(vertex)
    
for i in range(m):
    vertex = list(map(int, data[i+n+1].split()))
    m_vertex.append(vertex)
    
#################################

#시각화

import matplotlib.pyplot as plt

nx = [xy[0] for xy in n_vertex]
ny = [xy[1] for xy in n_vertex]

nx.append(nx[0])
ny.append(ny[0])

mx = [xy[0] for xy in m_vertex]
my = [xy[1] for xy in m_vertex]

mx.append(mx[0])
my.append(my[0])



plt.figure(figsize = (5,5))
plt.plot(nx, ny, marker = 'o')
plt.fill(nx, ny, alpha = 0.5)
plt.plot(mx, my, marker = 'o')
plt.fill(mx, my, alpha = 0.5)
plt.gca().set_aspect('equal')
plt.show()

############################## 답구현 gpt
#선분 교차점
import math

def ccw(A, B, C):
    return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])

def intersect(A, B, C, D):
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

def line_intersection(A, B, C, D):
    '''A,B: 첫 번째 선분의 양 끝점 / C,D: 두 번째 선분의 양 끝점'''
    a1, b1 = B[1] - A[1], A[0] - B[0]
    c1 = a1*A[0] + b1*A[1]
    a2, b2 = D[1] - C[1], C[0] - D[0]
    c2 = a2*C[0] + b2*C[1]
    det = a1*b2 - a2*b1
    if det == 0:
        return None  # 평행
    x = (b2*c1 - b1*c2) / det
    y = (a1*c2 - a2*c1) / det
    return [x, y]

#점이 폴리곤 안에 있는지 확인
def point_in_poly(p, poly):
    '''p: 점, poly: 폴리곤 꼭짓점 리스트'''
    x, y = p
    n = len(poly)
    inside = False
    for i in range(n):
        xi, yi = poly[i]
        xj, yj = poly[(i+1)%n]
        if ((yi > y) != (yj > y)) and (x < (xj-xi)*(y-yi)/(yj-yi)+xi):
            inside = not inside
    return inside

# 전체 교집합 로직
def polygon_intersection(poly1, poly2):
    points = []

    # 1. 서로 교차하는 모든 점
    for i in range(len(poly1)):
        A, B = poly1[i], poly1[(i+1)%len(poly1)]
        for j in range(len(poly2)):
            C, D = poly2[j], poly2[(j+1)%len(poly2)]
            if intersect(A, B, C, D):
                p = line_intersection(A, B, C, D)
                if p:
                    points.append(p)

    # 2. poly1 내부에 있는 poly2 점 추가
    for p in poly2:
        if point_in_poly(p, poly1):
            points.append(p)

    # 3. poly2 내부에 있는 poly1 점 추가
    for p in poly1:
        if point_in_poly(p, poly2):
            points.append(p)

    if not points:
        return None

    # 4. 점들을 시계 방향 정렬 (Convex Hull과 비슷)
    center = [sum(p[0] for p in points)/len(points), sum(p[1] for p in points)/len(points)]
    points.sort(key=lambda p: (math.atan2(p[1]-center[1], p[0]-center[0])))

    return points

#꼭짓점을 줫을때 넓이
def polygon_area(points):
    n = len(points)
    area = 0
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1)%n]  # 다음 꼭짓점, 마지막이면 처음으로
        area += (x1 * y2) - (x2 * y1)
    return abs(area) / 2


a = polygon_intersection(n_vertex, m_vertex)
polygon_area(a)
