
from collections import defaultdict

prime1000 = erathones(1000)   

def match(num_list): #vaild_pairs만들기
    de2 = defaultdict(list)
    for i in range(len(num_list)):
        for ii in range(len(num_list)):
            if i == ii:
                continue
            if num_list[i] + num_list[ii] in prime1000:
                de2[num_list[i]].append(num_list[ii])
    return de2

pairs = match(num_list)
paired = []
one_match = [item for k,v in pairs.items() if len(v)==1 for item in [k, v[0]]]
paired.append(one_match)


def match_one(pair_dict):
    
    첫수 매칭을 하고 시작하자
    pair_dict = pairs
    
    selected = [] #함수밖으로 빼야하고
    paired_dict_f_num = defaultdict(list) # 키 : 첫수와 매칭되는 숫자 키의 숫자 = 답
    f_num = list(pair_dict.keys())[0]
    for k, v in pair_dict.items():
        if len(v) == 1 and k not in selected:
            selected.append(k)
            selected.append(v[0])
            pairs = [num for num, v in pair_dict.items() if num not in selected]
            pair_dict = match(pairs)
        else:
            for i in range(len(pair_dict[f_num])):
                f_num_pair = pair_dict[f_num][i]
                selected.append(f_num)
                selected.append(f_num_pair)
                pairs = [num for num, v in pair_dict.items() if num not in selected]
                pair_dict = match(pairs)
        
            
            
    one_selection_keys = [k for k, v in pair_dict.items() if len(v) == 1 and k not in case]
    one_selection_keys2 = [item for k,v in pair_dict.items() if len(v)==1 for item in [[k, v[0]]]]
    
#### 
#1. 1:1대응
#2. 우선순위 -> 없어도될듯?
#3. 순차

#
def match_one(pair_dict, visited):
    
    
    if len(v) == 1 and k not in visited:
        
    