import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        final=s.lower().replace(" ","")
        
        for ch in string.punctuation:
            final = final.replace(ch, "")
        
        return final == final[::-1]