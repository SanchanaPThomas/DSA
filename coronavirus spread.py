# cook your dish here
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    
    min_infected=n
    max_infected=1
    
    for i in range(n):
        infected=[False]*n
        infected[i]=True
        count=1
        
        q=[i]
        
        while q:
            curr=q.pop(0)
            
            for j in range(curr-1,-1,-1):
                if not infected[j] and abs(x[curr]-x[j])<=2:
                    infected[j]=True
                    count+=1
                    q.append(j)
            for j in range(curr+1,n):
                if not infected[j] and abs(x[curr]-x[j])<=2:
                    infected[j]=True
                    count+=1
                    q.append(j)
        
        min_infected=min(min_infected,count)
        max_infected=max(max_infected,count)
        
    print(min_infected,max_infected)
