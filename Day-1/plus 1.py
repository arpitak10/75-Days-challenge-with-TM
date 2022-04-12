class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j=len(digits)-1 
        if len(digits)==1 and digits[-1]!=9:
            digits[-1]=digits[-1]+1
        else:
            for j in range(len(digits)-1,-1,-1):
                if digits[j]!=9 :
                    digits[j]=digits[j]+1 
                    break
                elif digits[j]==9:
                    digits[j]=0
            if j==0 and digits[j]==0: 
                digits.insert(0,1)
        return digits