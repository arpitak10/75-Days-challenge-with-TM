class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum1=0
        sum2=sum(nums)
        for i in range(len(nums)):
            if sum1==(sum2-sum1-nums[i]):
                return i
            sum1+=nums[i]
        return -1