class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res = []

        for i in range(2):
            for num in nums:
                res.append(num)
        return res