import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        final=s.lower().replace(" ","")
        for ch in string.punctuation:
            final = final.replace(ch, "")

        # final = final.lower()
        n=len(final)
        print(final)
        
        return final == final[::-1]