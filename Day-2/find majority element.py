class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_index=0
        count=0
        for i in range(len(nums)):
            if nums[i]==nums[max_index]:
                count+=1
            else:
                count-=1
            if count==0:
                max_index=i
                count=1
        count=0
        for i in range(len(nums)):
            if nums[i]==nums[max_index]:
                count+=1
        if count>len(nums)//2:
            return nums[max_index]
                