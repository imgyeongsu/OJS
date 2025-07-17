n = int(input())

num = list(map(int, input().split()))

min = num[0]+num[1]+num[2]
min_num1 = int()
min_num2 = int()
min_num3 = int()
for i in range(n-2):
    for ii in range(i+1,n-1):
        for iii in range(ii+1, n):
            hap = num[i] + num[ii] + num[iii]
            if abs(hap) < abs(min):
                min = hap
                min_num1 = num[i]
                min_num2 = num[ii]
                min_num3 = num[iii]
                
ans = [min_num1, min_num3, min_num2]
ans.sort()
for x in ans:
    print(x, end =' ')




def two_sum(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            return (left, right)
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return None

nl = [1,2,3,4,5,6]

two_sum(*nl)