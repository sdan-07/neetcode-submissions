class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        numarr = list(numset)
        numarr.sort()
        n = len(numarr)
        if n<2: return n
        longest = float("-inf")
        i = j = 0

        # 0,1,2,3,4,5,6
        while j < n - 1:
            if abs(numarr[j] - numarr[j + 1]) != 1:
                size = j - i + 1
                longest = max(longest, size)
                j += 1
                i = j
            elif j == n - 2 and abs(numarr[j] - numarr[j + 1]) == 1:
                size = j - i + 2
                longest = max(longest, size)
                break
            else:
                j += 1
        return longest
