class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead
        .
        """
        non_zero=0
        zero=nums.index(0)
        for k in range(len(nums)):
            if nums[k]!=0:
                non_zero=i
        while zero<len(nums):
            nums[zero],nums[non_zero]=nums[non_zero],nums[zero]
            