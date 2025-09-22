for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a_set=set(a)
    count=0
    for i in b:
        if i in a_set:
            count+=1
    print(count)
