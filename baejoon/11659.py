import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cum_sum = [0] * (n +1)
num_list = list(map(int, input().split()))
for i in range(n):
    cum_sum[i+1] = cum_sum[i] + num_list[i]

for _ in range(m):
    s, e = map(int,input().split())
    print(cum_sum[e] - cum_sum[s-1])
 