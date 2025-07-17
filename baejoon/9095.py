T = int(input())

a = [0] * 11
a[1], a[2], a[3] = 1, 2, 4
def hapfrom123(number):
    i = 4
    if number <i:
        return a[number]
    else:
        while i <= number:
            a[i] = a[i-1] + a[i-2] + a[i-3] # 제일 처음 숫자를 각각 1 2 3으로 고정했을때 뒤에 나올수 있는 경우의 수
            i += 1
        return a[number]

n = []
for _ in range(T):
    n.append(int(input()))
    
for i in n:
    print(hapfrom123(i))
        
