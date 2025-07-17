N = int(input())


xlist = list(map(int, input().split()))
  

xsort = sorted(xlist)

result = {}
result[xsort[0]] = 0
lnum = 0
for i in range(1,len(xsort)):
    if xsort[i] != xsort[i-1]:
        lnum+=1
        result[xsort[i]] = lnum
        
for i in xlist:
    print(result[i], end = ' ')