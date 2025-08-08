T = int(input())

for t in range(1,T+1):
    string = input()
    result = ''
    left, right = 0, len(string)-1

    while left <= right: #이분탐색 시작
        
        if left == right: # 같아지면 남은거 더하고 그만
            result += string[left]
            break         

        if string[left] > string[right]: # 우측 문자열이 우선 일때
            result += string[right] 
            right -= 1
        elif string[left] < string[right]:
            result += string[left]
            left += 1
        else: # 좌 우측 문자가 같을때 <<<<<< 좌우를 동시에 탐색하다가 먼저 작아질때 그 부분을 추가
            check_left, check_right = left, right # 그 시점 좌우 인덱스 저장
            while check_left < check_right and string[check_left] == string[check_right]: # 좌우가 같고, 탐색중인 우측 인덱스가 더 크다면 하나씩 더 탐색
                check_left += 1
                check_right -= 1

            if check_left >= check_right or string[check_left] <= string[check_right]: # 탐색 중 좌측에 먼저 작은 값이 나타나거나 범위를 넘어버리면 #좌측값을 추가
                result += string[left]
                left += 1 
            else: #아니면 우측값 추가
                result += string[right]
                right -= 1
    
    print(f'#{t} {result}')

        