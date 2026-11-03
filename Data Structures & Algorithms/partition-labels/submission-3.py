class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_index = {}
        for i, c in enumerate(s):
            end_index[c] = i

        res = []
        size, end = 0, 0
        for i, c in enumerate(s):
            size += 1
            end = max(end_index[c], end)
            
            if i == end:
                res.append(size)
                size = 0
        
        return res

        # def merge_intervals(intervals):
        #     res = [intervals[0]]
        #     for s, e in intervals[1:]:
        #         prevE = res[-1][1]
        #         if s < prevE:
        #             res[-1][1] = max(e, prevE)
        #         else:
        #             res.append([s, e])
            
        #     return res

        # index_map = {} # char: [start, end]
        # for i, c in enumerate(s):
        #     if c in index_map:
        #         index_map[c][1] = i
        #     else:
        #         index_map[c] = [i, i]
        
        # intervals = list(index_map.values())
        # merged_intervals = merge_intervals(intervals)
        # res = [(e - s + 1) for s, e in merged_intervals]

        # return res