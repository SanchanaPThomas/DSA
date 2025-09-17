def solve():
    s=input()
    n=len(s)
    count=0
    i=0
    while i<n-1:
        if s[i]!=s[i+1]:
            count+=1
            i+=2
        else:
            i+=1
    print(count)
    
t=int(input())
for _ in range(t):
    solve()
