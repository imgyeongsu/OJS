T = int(input())

import math


for _ in range(T):
    B, W, x, y, z = map(int, input().split())
    # B: 검은 공, 상자 수
    # W: 흰 공, 상자 수
    # X: 검은상자에 검은 공 점수
    # Y; 흰상자에 흰 공 점수
    # Z: 반대 색상 점수
    less = min(B,W)
    best_score = -math.inf
    if less ==B:
        for change in range(B+1):
            BinB = B - change
            WinW = W - change
            score = BinB * x + WinW * y + change * z *2 
            if score > best_score:
                best_score =score
    else:
        for change in range(W+1):
            BinB = B - change
            WinW = W - change
            score = BinB * x + WinW * y + change * z * 2
            if score > best_score:
                best_score =score
    print(best_score)
    
    
    # BinB = 0 #검은 상자안에 있는 검은 공의 수
    # WinW = 0 #흰 상자안에 있는 흰 공의 수
    # remain = B + W - ( BinB + WinW )

    # best_score = -10000000
    # #모든 경우의 수 탐방
    # for : #아 두개 엮여있음 둘중 작은 걸 for문에 넣고 교체 되는거 고정
    #     for WinW in range(W+1):
    #         remain = B + W - (BinB + WinW)
    #         score = BinB * x + WinW * y + remain * z
    #         if score > best_score:
    #             best_score = score

    # print(best_score)

