class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        def bsearch(nums, target, l, r):
            
            if l > r: return -1

            mid = l+(r-l)//2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                return bsearch(nums, target, l+1, r)
            else:
                return bsearch(nums, target, l, r-1)

        return bsearch(nums, target, 0, n-1) 