
MOD = 1_000_000_007


def fact_mod(x):
    fact = 1
    for i in range(1,x+1):
        fact = (fact * i) % MOD

    return fact

##################################################################

import random

l = [i for i in range(1,41)]
random.shuffle(l)

l #순열
n = len(l) #순열의 크기
already = [] #각 순열을 계산할때 이미 나온 원소 <- 사실 이건 그냥 순열인데?
fct = [] #각 순열의 위치에서 계산해줘야 하는 factorial

# 순열의 첫 원소부터 계산
for i in range(n):
    #미리 나온 원소빼는작업 부터 해야함
     #l[i] < already[:i] <- 해당하는 원소의 갯수만큼 아랫식에서 빼주면 된다
    alreadyi = l[:i] 
    already_com = [ii for ii in alreadyi if ii > l[i]] 
    n_already = len(already_com)
    
    f = l[i] - i - n_already
    ff = fact_mod(f)
    fct.append(ff)
    

for i in range(n):
    print(i+1, l[i], fct[i])


###############################################################    
    
def sequence_p(permutation):
    l = permutation

    n = len(l) #순열의 크기
    # already = [] #각 순열을 계산할때 이미 나온 원소 <- 사실 이건 그냥 순열인데?
    fct = [] #각 순열의 위치에서 계산해줘야 하는 factorial

    # 순열의 첫 원소부터 계산
    for i in range(n):
        #미리 나온 원소빼는작업 부터 해야함
         #l[i] < already[:i] <- 해당하는 원소의 갯수만큼 아랫식에서 빼주면 된다
        alreadyi = l[:i] 
        already_com = [ii for ii in alreadyi if ii > l[i]] 
        n_already = len(already_com)
        
        f = l[i] - i - n_already  #이부분이 뭔가 잘못됏음 수식이 조금더 복잡해야한다 1~15테스트케이스로 테스트
        ff = fact_mod(f)
        fct.append(ff)
        
    ans = 1
    for x in fct:
        ans = (ans * x) %MOD
        
    return ans
        

testcase1 = list(map(int, input().split()))

sequence_p(testcase1)


fact_mod(14)