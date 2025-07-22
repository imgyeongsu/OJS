n = int(input())
info = list(map(int, input().split()))

loc = [0] * n # 사람들의 위치를 저장할 


for i in range(1, n+1): #1번 사람부터 n번 사람까지
    zero_index = [idx for idx, v in enumerate(loc) if v == 0] # 0값을 가지는 loc의 인덱스
    loc[zero_index[info[i-1]]] = i # i번 사람 앞에 info[i-1]명 만큼의 빈 자리가 있도록 해당 위치에 배치 --> 왜냐 이후에 들어가는 사람들은 다 키가 크니까

print(*loc)