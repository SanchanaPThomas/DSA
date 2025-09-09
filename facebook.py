t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # your code goes here
    most_popular_index = 0  

    for i in range(1, n):
        if a[i] > a[most_popular_index]:
            most_popular_index = i
        elif a[i] == a[most_popular_index] and b[i] > b[most_popular_index]:
            most_popular_index = i

    print(most_popular_index + 1)
