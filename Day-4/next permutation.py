class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = len(nums) - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
        if i > 0:
            while j >= i:
                if nums[j] > nums[i-1]:
                    break
                j -= 1
            nums[i-1], nums[j] = nums[j], nums[i-1]
            j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1