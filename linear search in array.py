a,b=map(int,input().split())
l=list(map(int,input().split()))
for i in l:
    if i==b:
        print('yes')
        break
else:
    print('no')
