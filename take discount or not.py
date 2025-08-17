t = int(input())

while t > 0:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    s=0
    m=0
    for i in a:
        m+=i
        if i-y>0:
            s+=(i-y)
        else:
            s+=0
    if (s+x)<m:
        print('coupon')
    else:
        print('no coupon')
