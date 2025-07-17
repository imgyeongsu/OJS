t = int(input())

n = int(input())
nums = list(map(int, input().split()))

# nums = [4,5,6,3,1,2,7,8,9]
nums.append(999) #빈칸 추가

# nums = [9,5,6,3,1,2,7,8,4,999] #1
# nums = [999,5,6,3,1,2,7,8,4,9] #5
# nums = [1,5,6,3,999,2,7,8,4,9]
# nums = [1,999,6,3,5,2,7,8,4,9]
# nums = [1,2,6,3,5,999,7,8,4,9]
# nums = [1,2,999,3,5,6,7,8,4,9]
# nums = [1,2,3,999,5,6,7,8,4,9]
# nums = [1,2,3,4,5,6,7,8,999,9]
# nums = [1,2,3,4,5,6,7,8,9,999]

log = []
# nums =[1,2,3]
#처음꺼 바꾸는거 만약 제일 큰숫자가 제자리에 있다면? 똑같이 동작하긴 하는데
idx2 = nums.index(999)
idx1 = nums.index(idx2)

nums[idx1] = 999
nums[idx2] = idx2

log.append(idx1+1)

nums
log
#종료까지 코드
while nums[-1] != 999:

    idx3 = nums.index(999)+1 #왜 1을 더하는가 +1한 위치를 찾아야하니까
    idx4 = nums.index(idx3)

    nums[idx4] = 999
    nums[idx3-1] = idx3 # 왜 1을 빼는가 변경되야할 위치는 -1해야 정확하니까

    log.append(idx4 + 1)

    nums
    log

print(len(log))
for i in log:
    print(i, end=' ')