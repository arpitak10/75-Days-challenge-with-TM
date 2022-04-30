class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev_sum={}
        res=0
        curr_sum=0
        for i in nums:
            curr_sum+=i
            if curr_sum==k:
                res+=1 
            if curr_sum-k in prev_sum:
                res+=prev_sum[curr_sum-k]
            prev_sum[curr_sum]=prev_sum.get(curr_sum,0)+1 
        return res
        