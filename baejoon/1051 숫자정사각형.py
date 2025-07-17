n, m = map(int, input().split())
matrix = []

for _ in range(n):
    nums = [s for s in input()]
    matrix.append(nums)

#가장 큰걸 찾고 #점점 작게 찾아나간다
largest_length = min(n,m)-1 #가장 큰 변의 길이

for i in range(largest_length): # 0, 1, 2, largets-2
    l = largest_length - i # 가장 긴 변부터 1까지 larget .... 
    #x가 끝까지 될때까지
    for xi in range(m-l):
        for yi in range(n-l):
            dx = xi + l
            dy = yi + l
            if matrix[yi][xi] == matrix[yi][dx] == matrix[dy][xi] == matrix[dy][dx]:
                print((l+1)**2)
                exit()

print(1)
                
            
    
