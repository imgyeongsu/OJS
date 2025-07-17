from collections import defaultdict


def erathones(limit):
    sieve = [True]*(limit+1)
    sieve[0] = sieve[1] = False
    
    for num in range(2, int((limit**0.5)/2)):
        if sieve[num]:
            for not_prime in range(num **2, limit+1, num):
                sieve[not_prime] = False
                
    return [n for n, is_prime in enumerate(sieve) if is_prime]
        


prime1000 = erathones(1000)        

num_list = [1, 4, 7, 10, 11, 12]
num_list = [34, 39, 32, 4, 9, 35, 14, 17]
num_list = [8, 9, 1, 14]
num_list_without_1_1 = [34, 39,  4, 9]
first_num = num_list[0]

#match함수와 동일한 기능 근데 아래함수가 더 빠를듯
di = {}
for i in num_list:
    make_prime = [prime - i for prime in prime1000 if prime > i]
    match_number =[]
    for ii in num_list:
        if ii in make_prime:
            match_number.append(ii)
    
    di[i] = match_number


def match(num_list): #vaild_pairs만들기
    de2 = defaultdict(list)
    for i in range(len(num_list)):
        for ii in range(len(num_list)):
            if i == ii:
                continue
            if num_list[i] + num_list[ii] in prime1000:
                de2[num_list[i]].append(num_list[ii])
    return de2
len(match(num_list))
#match함수의 결과가 홀수이거나 없는 원소가 있다 -1출력
pairs = match(num_list)
def coupling(pairs): #num_dict은 match함수의 결과물
    if len(num_dict) % 2 == 1:
        return -1
    #set을 담고 있는 리스트로 반환
    case = []
    case_count = 0
    #벨류값을 하나 가지고 있는 키값을 커플링
    one_one_match = [item for k,v in pairs.items() if len(v)==1 for item in [k, v[0]]] #쌍방인거 체크함? 자동임
    if one_one_match: # 다음 파일 match_one 함수 실행
        pop_list = [num for num, v in pairs.items() if num not in one_one_match] #변수명 remain_pairs와 동일
        pairs = match(pop_list) # 여기서 다시 매칭을 해버리면 시간복잡도가 많이 올라갈거같음 안하고 하는 방법 고민 <- 이걸 만들어야 빨리끝남
        #굳이 삭제를 하지말고 앞으로 대안을 찾을때 매칭된 숫자를 제하고 매칭을 시키면 될거같음
        case.append(one_one_match)
    else:
        first_number = list(pairs.keys())[0]
        for i in range(first_number):
            suppose_pairing = [first_number, pairs[first_number][case_count]] #case_count = i
            case.append(suppose_pairing)
            remain_pairs = [num for num, v in pairs.items() if num not in suppose_pairing]
            pairs = match(remain_pairs)
            
        
#원원매칭을 해서 최대한 없애기 if oneonemat
#원원 매칭 할 건덕지가 없다면 직접 매칭하기 경우의수 카운터하면서 수가 많아지면 엄청 기어들어가야할거같은데
#안에 있는 리스트가 전부 빌때까지 while Pairs:
#미친듯이 느릴거같은데
    
    
    




    
de2를 기준으로 1, 4, 7, 10을 짝지을거고
1: 4, 10
4: 1, 7
7: 4, 10
10: 1, 7

을 짝지을수 있다고 하면 경우의 수         
무식하게 접근하면 일단 1,4를 짝지어서 해결되는지 보고 안되면 1,10을 짝지어보고 이런식으로 가는방법이있고
좀 고급지게 하고싶은데 스도쿠 느낌이 살짝난다

다시 최초 match해서 1ㄷ1인거 빼고 다시 match 1ㄷ1인게 없다면 첫숫자와 바로 다음거 빼고 맷취해서 0이 나오면

kv = match(num_list)
one_one_match = [item for k,v in kv.items() if len(v)==1 for item in [k, v[0]]]
num_list = [num for num in num_list if num not in one_one_match]

kv2 = match(num_list)
one_one_match2 = [item for k,v in kv2.items() if len(v)==1 for item in [k, v[0]]]

if one_one_match2:
    #다시 차집합
    print('')
else:
   matchingnum = [first_num, kv2[first_num][0]] #반복 들어가야지 index가 끝까지
   num_list3 = [num for num in num_list if num not in matchingnum]
   kv3 = match(num_list3)
   

#다시 의사결정코드
# vaild_pairs를 만듬
# 단일 값 제거
# 이중값 이상일시 제일 첫 인수 매칭시키고 반복
