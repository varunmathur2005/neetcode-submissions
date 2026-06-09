class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        '''
        1). if the start of the current interval < the start of new interval and
        the end of new interval < the start of the next interval - no merging
        
        '''
        res = []
        for i in range(len(intervals)):
            curS, curE = intervals[i]
            if curS > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > curE:
                res.append(intervals[i])
            else:
                newInterval = [min(curS, newInterval[0]), max(curE, newInterval[1])]
        
        res.append(newInterval)
        return res
