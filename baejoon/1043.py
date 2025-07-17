n, p = map(int, input().split())
t = list(map(int, input().split()))
tn = t[0] #진실을 아는 사람수
tmans = t[1:] #진실을 아는 사람
party = {}
for i in range(p):
    input_party = list(map(int, input().split()))
    party[i] = input_party[1:]

party
tmans
#파티가 열렸는데 Tmans이 그 파티에 있었다 그럼 그 파티인원들도 다 Tman이되는거지

participate = 0
for i in range(p): #파티가 순차적으로 열린다
    mans = party[i] #파티에 참여하는 사람
    for ii in mans: #참여하는 사람들에 대해서
        if ii in tmans: #만약 진실을 아는 사람들이 있다면
            tmans = tmans + mans # 파티에 참여하는 사람들은 Tman이 된다
        #### 이 아래부분 최대값을 구해야함
        #어떻게 최대값을 구하느냐 최대한 적은 사람이 참여하는 파티부터 가면된다
        #그러면 위에서 value값이 적은 순서대로 정렬하고 진행하면 답이 나온다
         # 반례
          # 12 
          # or
          # 2345    
          # 16789    
          
        #그렇다면 일단 갈수있는 파티를 모두 얻은 다음 참가인원이 적은 순서대로 참여하면 웬만하면 될거같음
        
        #참여
        else: #참여하는 사람들중 진실을 아는사람이 없다.
            participate += 1 #그파티에 참여를 하고 그 사람은 tman이 된다
            tmans = tmans + mans

#tman이 없는 파티를 골라야함

