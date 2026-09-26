class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        
        res=[0]*n

        for i in range(n-1):
            greatest=-1
            for j in range(i+1,n):
                greatest = max(greatest, arr[j])
            res[i] = greatest
        res[-1] = -1

        return res