t = int(input())

while t > 0:
    x, y = map(int, input().split())
    if y>x:
        print(x+2*(y-x))
    else:
        print(y)
    t -= 1
