import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        final=s.lower().replace(" ","")
        for ch in string.punctuation:
            final = final.replace(ch, "")

        # final = final.lower()
        n=len(final)
        print(final)
        l,r = 0,n-1

        while l<r:
            if final[l] != final[r]:
                return False
            l+=1
            r-=1
        return True