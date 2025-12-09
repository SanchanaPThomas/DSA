class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        jumps=0
        current_end=0
        farthest=0
        for i,jump in enumerate(nums[:-1]):
            farthest=max(farthest,i+jump)
            if i==current_end:
                jumps+=1
                current_end=farthest
            if current_end>=n-1:
                break
        return jumps
