pairs=[]
for _ in range(int(input())):
    pair=tuple(map(int,input().split()))
    pairs.append(pair)

a,b=map(int,input().split())
for x,y in pairs:
    if (x==a and y==b) or (x==b and y==a):
        print('yes')
        break
else:
    print('no')
