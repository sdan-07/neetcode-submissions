class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zeros=0
        for num in nums:
            if num==0:
                zeros += 1
            else:
                prod *= num

        res=[]
        for num in nums:
            if zeros == 1:
                if num == 0:
                    val = prod
                else:
                    val = 0
            elif zeros > 1:
                val = 0

            else: val = prod // num
            res.append(val)

        return res