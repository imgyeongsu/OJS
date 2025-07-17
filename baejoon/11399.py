n = int(input())

pi = list(map(int, input().split()))

sorted_pi = sorted(pi)

total_time = 0
for i in range(n):
    total_time += sorted_pi[i] * (n-i)
    
print(total_time)