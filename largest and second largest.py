t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    a_set=set(a)
    b=list(a_set)
    b.sort()
    print(b[-1]+b[-2])
