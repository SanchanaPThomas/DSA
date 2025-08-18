t = int(input())

while t > 0:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s=0
    for i in range(len(a)):
        if a[i]>=x:
            s+=b[i]
    print(s)
    t -= 1
