class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def merge_intervals(intervals):
            res = [intervals[0]]
            for s, e in intervals[1:]:
                prevE = res[-1][1]
                if s < prevE:
                    res[-1][1] = max(e, prevE)
                else:
                    res.append([s, e])
            
            return res

        index_map = {} # char: [start, end]
        for i, c in enumerate(s):
            if c in index_map:
                index_map[c][1] = i
            else:
                index_map[c] = [i, i]
        
        print(index_map)
        intervals = list(index_map.values())
        merged_intervals = merge_intervals(intervals)
        print(merged_intervals)
        res = [(e - s + 1) for s, e in merged_intervals]

        return res