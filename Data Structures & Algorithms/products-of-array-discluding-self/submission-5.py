class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros=0
        prod=1
        for num in nums:
            if num == 0:
                zeros+=1
            else:
                prod *= num

        res=[0]*len(nums)
        if zeros > 1 :
            return res
        
        for i in range(len(nums)):
            if zeros == 1 and nums[i] == 0:
                res[i] = prod
            elif zeros != 1:
                res[i] = prod // nums[i]

        return res