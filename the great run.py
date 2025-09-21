for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    
    max_sum=sum(a[:k])
    current_sum=max_sum
    
    for i in range(k,n):
        current_sum=current_sum-a[i-k]+a[i]
        max_sum=max(max_sum,current_sum)
        
    print(max_sum)
