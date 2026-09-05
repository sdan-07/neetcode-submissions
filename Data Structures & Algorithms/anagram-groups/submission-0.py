class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))

            anag=[]
            if sorted_str not in d:
                anag.append(strs[i])
                d[sorted_str] = anag
            else:
                d.get(sorted_str).append(strs[i])

        res=[]
        for k,v in d.items():
            res.append(v)

        return res