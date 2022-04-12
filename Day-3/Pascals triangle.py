class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst=[]
        i=1
        if i==1:
            lst.append([1])
            i+=1
        if numRows==1:
            return lst
        if i==2:
            lst.append([1,1])
            i+=1
        if numRows==2:
            return lst
        for i in range(3,numRows+1):
            temp=[1]
            #print(len(lst[1]))
            for j in range(len(lst[i-2])-1):
                temp.append(lst[i-2][j]+lst[i-2][j+1])
            temp.append(1)
            lst.append(temp)
        return lst
                         
                