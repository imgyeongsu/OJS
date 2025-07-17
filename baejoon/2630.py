from collections import deque
n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
   

def seperate(arr, n):
    nn = n//2
    arr1 = [row[:nn] for row in arr[:nn]]
    arr2 = [row[nn:] for row in arr[:nn]]
    arr3 = [row[:nn] for row in arr[nn:]]
    arr4 = [row[nn:] for row in arr[nn:]]
    return arr1, arr2, arr3, arr4

def need_cut(arr, length):
    blue = len([cell for row in arr for cell in row if cell == 1])
    white = len([cell for row in arr for cell in row if cell == 0])
    if max(blue, white)  == length ** 2:
        return False
    else:
        return True
    
queue = deque()
queue.append(arr)
white = 0
blue = 0

while queue:
    paper = queue.popleft()
    length = len(paper)
    
    if length ==1:
        if paper[0][0] == 0 :
            white += 1
        else:
            blue += 1
        continue
    
    if not need_cut(paper,length):
        if paper[0][0] == 0:
            white +=1
        else:
            blue += 1
    else:
        arr1, arr2, arr3, arr4 = seperate(paper, length)
        queue.extend([arr1, arr2, arr3, arr4])

print(white)
print(blue)


while queue:
    n = n//2
    paper = queue.popleft()
    if paper:
        if sum2dar(paper) in [0, len(paper) ** 2]:
            ans += 1
        else: #애초에 빈걸 추가시키면 안됨
            arr1 = paper[:n][:n] #이 부분도 잘못됨
            arr2 = paper[:n][n:]
            arr3 = paper[n:][:n]
            arr4 = paper[n:][n:]
            queue.append(arr1)
            queue.append(arr2)
            queue.append(arr3)
            queue.append(arr4)
        
aaa =[[1,1,1,1],[1,1,1,1]]

[cell for row in aaa for cell in row if cell == 1]
[cell for row in aaa for cell in row if cell == 0]
[cell for row in aaa for cell in row]



