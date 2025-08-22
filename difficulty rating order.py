t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    if d==sorted(d):
        print('yes')
    else:
        print('no')
    t -= 1
