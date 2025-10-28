class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr=[1]*len(nums)
        p=1
        for i in range(1,len(nums)):
            arr[i]=arr[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            p=p*nums[i+1]
            arr[i]*=p
        return arr
