t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))

    minimum = min(a)
    count = 0
    for element in a:
        if element != minimum:
            count += 1

    print(count)
    t -= 1
