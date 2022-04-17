class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[]
        n=len(nums)
        ans=[-1]*n
        i=0
        
        for i in range(2*n-1,-1,-1):
            while len(stack)>0 and nums[stack[-1]]<=nums[i%n]:
                stack.pop()
            if len(stack)>0:
                
                ans[i%n]=nums[stack[-1]]
            else:
                ans[i%n]=-1
            stack.append(i%n)
            #i+=1
        return ans