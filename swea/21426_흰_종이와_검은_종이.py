T = int(input())

white_paper = list(map(int, input().split()))
black_paper1 = list(map(int, input().split()))
black_paper2 = list(map(int, input().split()))

#교집합 함수와 #합집합 함수
#w와 b1의 교집합 wb1
#w와 b2의 교집합 wb2
# wb1과 wb2의 합집합 wb
# wb와 w의 교집합 판단

#차집합 w -b1 , w -b2 햇을때 남는 게잇는가

# b을 합치고 그 안에 w가 있는지 판단

#볼록다각형으로 분리해서 계산하면 될듯
