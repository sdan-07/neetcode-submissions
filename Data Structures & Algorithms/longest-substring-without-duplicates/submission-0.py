class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        longest = -1

        cset = set()
        i=j=0

        while j<len(s):
            while s[j] in cset:
                cset.remove(s[i])
                i+=1

            cset.add(s[j])   
            size = j-i+1
            longest = max(longest, size)
            j+=1
        return longest