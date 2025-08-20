t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    happy_days=0
    for i in range(n):
        if (2*a[i])>=b[i] and (2*b[i])>=a[i]:
            happy_days+=1
    print(happy_days)
            
