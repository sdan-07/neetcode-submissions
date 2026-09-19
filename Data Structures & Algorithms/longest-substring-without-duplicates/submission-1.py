class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        n=len(s)
        longest = -1

        cset = set()
        i=j=0
        while j<n:
            while s[j] in cset:
                cset.remove(s[i])
                i+=1

            cset.add(s[j])
            longest = max(longest, j-i+1)
            j+=1

        return longest