class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for pas in details:
            age = int(pas[-4:-3+1])
            if age > 60:
                count+=1
        return count