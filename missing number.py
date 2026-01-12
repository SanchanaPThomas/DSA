def missingNumber(nums):
    n = len(nums)
    ans = 0
    
    for i in range(n + 1):
        ans ^= i   # XOR all numbers from 0 to n

    for x in nums:
        ans ^= x   # XOR all given numbers
    
    return ans
