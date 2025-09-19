for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    
    distinct_arr=[]
    if n>0:
        distinct_arr.append(arr[0])
        for i in range(1,n):
            if arr[i]!=arr[i-1]:
                distinct_arr.append(arr[i])
                
    print(len(distinct_arr))
    print(*distinct_arr)
