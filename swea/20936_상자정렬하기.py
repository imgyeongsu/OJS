t = int(input())

for _ in range(t):
    
    n = int(input())
    nums = list(map(int, input().split()))
    
    good = [i+1 == nums[i] for i in range(n)]
    if n == sum(good):
        print(0)
        print()

    else:
        try :
            biggest_wrong = max([nums[i] for i in range(n) if not good[i]])
        except:
            biggest_wrong = n

        log = []
                
        nums.append(999) #빈칸 추가
        idx2 = nums.index(biggest_wrong) # 제자리가 아닌 상자 중 가장 큰 상자의 인덱스

        #가장 큰 상자 맨 뒤로 빼기
        nums[idx2] = 999 
        nums[-1] = biggest_wrong

        #제일 큰 숫자가 들어있던 칸의 번호
        log.append(idx2+1)

        while nums[-1] != 999:

            idx3 = nums.index(999)+1 #빈칸의 상자 번호
            idx4 = nums.index(idx3) #빈칸 번호와 같은 상자가 위치한 칸의 번호

            nums[idx4] = 999 #상자 이동해서 빈칸이 됨
            nums[idx3-1] = idx3# 빈칸에 알맞은 상자를 넣음

            log.append(idx4 + 1) #이동한 상자의 칸 번호

        print(len(log))
        for i in log:
            print(i, end=' ')

# test case

#통과
# 3
# 1 2 3

#통과
# 4
# 2 3 4 1

#통과
# 6
# 1 2 3 5 4 6

