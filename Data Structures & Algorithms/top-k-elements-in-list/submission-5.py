class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        freq=Counter(nums)
        bucket=[[] for i in range(len(nums)+1)]

        for key,val in freq.items():
            lst=[]
            if not bucket[val]: 
                lst.append(key)
                bucket[val] = lst
            else:
                bucket[val].append(key)
        # print(bucket)

        for i in range(len(bucket)-1, 0, -1):
            for val in bucket[i]: 
                res.append(val)
                if len(res) == k:
                    return res
        