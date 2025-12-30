import math
def largest_adjacent_lcm(arr):
    max_lcm=0
    for i in range(len(arr)-1):
        a,b=arr[i],arr[i+1]
        lcm=(a*b)//math.gcd(a,b)
        max_lcm=max(max_lcm,lcm)
    return max_lcm
