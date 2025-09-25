def sortArrayByParity(nums):
    even=[]
    odd=[]
    for i in nums:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return odd+even

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))

    result=sortArrayByParity(nums)

    print(" ".join(map(str,result)))
