class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for s in strs:
            freq = self.frequency(s)
            anag=[]
            if freq not in d:
                anag.append(s)
                d[freq] = anag
            else:
                d.get(freq).append(s)
        
        res=[]   
        for k,v in d.items():
            res.append(v)

        return res

    def frequency(self, s):
        count_str = ""
        lst = [0] * 26

        for ch in s:
            lst[ord(ch) - ord("a")] += 1

        return "#".join(map(str, lst))
        
