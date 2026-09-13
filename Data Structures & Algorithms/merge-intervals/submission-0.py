class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        intervals.sort()
        n = len(intervals)
        if n<2: return intervals

        while i < n - 1:
            if not res:
                if intervals[i + 1][0] <= intervals[i][1]:
                    res.append([intervals[i][0], max(intervals[i + 1][1], intervals[0][1])])
                else:
                    res.append(intervals[i])
                    res.append(intervals[i+1])
                    j+=1
            
            elif intervals[i + 1][0] <= res[j][1]:
                res[j][1] = max(intervals[i + 1][1], res[j][1])

            elif intervals[i + 1][0] > res[j][1]:
                res.append(intervals[i + 1])
                j += 1

            i += 1
        return res
