class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        first_index=0
        last_index=0
        for i in range(len(nums)):
            d[nums[i]]=i
        for i in range(len(nums)):
            if target-nums[i] in d and d[target-nums[i]]!=i :
                first_index=i
                last_index=d[target-nums[i]]
                break
        return [first_index,last_index]