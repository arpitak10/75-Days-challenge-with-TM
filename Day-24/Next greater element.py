class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        ans=[]
        for i in range(len(nums2)-1,-1,-1):
            while len(stack)>0 and stack[-1]<nums2[i]:
                stack.pop()
            if len(stack)==0:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            #print(nums2[i])
            stack.append(nums2[i])
        ans.reverse()
        #print(ans)
        ans2=[]
        for i in range(len(nums1)):
            s1=nums2.index(nums1[i])
            ans2.append(ans[s1])
        return ans2