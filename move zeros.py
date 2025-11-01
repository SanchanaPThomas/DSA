class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
      
        pos = 0  # position for next non-zero
    
    # First pass: move all non-zeros forward
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos] = nums[i]
                pos += 1
    
    # Second pass: fill remaining with zeros
        for i in range(pos, len(nums)):
            nums[i] = 0
