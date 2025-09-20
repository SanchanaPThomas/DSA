for _ in range(int(input())):
    n,b=map(int,input().split())
    a=list(map(int,input().split()))
    seen = set()
    found = False
    for num in a:
        if (num + b) in seen or (num - b) in seen:
            found = True
            break
        seen.add(num)
    
    if found:
        print(1)
    else:
        print(0)
