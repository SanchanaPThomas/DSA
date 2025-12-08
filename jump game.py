class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        reach=0
        for i,jump in enumerate(nums):
            if i>reach:
                return False
            reach=max(reach,i+jump)
            if reach>=n-1:
                return True
        return True
