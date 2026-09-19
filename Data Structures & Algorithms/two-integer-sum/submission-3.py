class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        n=len(nums)
        res=[]

        for i,num in enumerate(nums):
            map[num] = i
        
        for i in range(n):
            diff = target - nums[i]

            if diff in map and map[diff] != i:
                res.append(i)
                res.append(map[diff])
                return res

        return res[0]