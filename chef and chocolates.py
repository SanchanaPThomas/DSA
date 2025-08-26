t = int(input())

while t > 0:
    x, y, z = map(int, input().split())
    total_rupees = (x * 5) + (y * 10)
    max_chocolates = total_rupees // z
    print(max_chocolates)
    t -= 1
