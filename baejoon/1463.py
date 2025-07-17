n = int(input())

stack = 0
while n != 1:
    if n % 3 == 0:
        n /= 3
    elif n % 2 == 0:
        n /= 2
    else:
        n -= 1
    stack +=1
    
print(stack)
