t = int(input())
for _ in range(t):
    x, y, z = map(int, input().split())
    if x == min(x, y, z):
        print('ALICE')
    elif y == min(x, y, z):
        print('BOB')
    else:
        print('CHARLIE')
