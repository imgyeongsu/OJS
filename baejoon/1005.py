class ACMcraft:
    def __init__(self, tech, delay):
        self.ready = False #이전 건물 다 지어졌는지 여부
        self.delay =  delay
        self.require = []
                
    def build(self): #시간 구하기
        if self.tech == 1:
            self.totaldelay = self.delay
        else:
            n = len(self.need)
            self.totaldelay = self.delay + max([self.need[i].totaldelay for i in range(n)]) 
            # 필요한 건물 중 가장 오래걸리는 시간 더하기
                


t = int(input()) # T입력
for i in range(t): # t 번 반복
    n, k = map(int, input().split()) #
    
    ds = [int(d) for d in input().split()] # 건설 완료 시간 입력
    
    xy = [] #건설 순서 리스트 
    for ii in range(k): # 건설 순서 정보 저장
        x1, y1 = map(int, input().split())
        xy.append([x1,y1])
        
    w = int(input()) #목표 입력



    
    
    tec = {}
    for iii in range(1,n+1):
        tec[iii] = ACMcraft(iii, delay = ds[iii-1])
    
    for a in xy:
        tec[a[1]].need.append(tec[a[0]])
    
    
    for i in range(w):
        tec[i+1].build()
    
    print(tec[w].totaldelay)




tec[4].need[0].tech

tec[1].build()
tec[1].totaldelay
tec[2].build()
tec[2].totaldelay
tec[3].build()
tec[3].totaldelay
tec[4].build()
tec[4].totaldelay


#재귀 함수로 가자

techtree =()
def build(tech, techtree):
    if tech == 0:
        return techtree
    else:
        n = len(tec[tech].need)
        for i in range(n):
            techtree = [tec[tech].need[0]]
        

from collections import deque
dq = deque((1,2,3))

dq.appendleft(1)



def techtree(w, techtree):
    tl = techtree
    tl.append(w)
    n = len(tec[w].need)
    for i in range(n):
        w = tec[w].need[i].tech
        if w == 1:
            return tl
        else:
            techtree(w,tl)

tectree = []
techtree(4, tectree)
