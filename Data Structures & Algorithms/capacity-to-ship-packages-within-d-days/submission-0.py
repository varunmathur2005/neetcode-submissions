class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        heaviest_package <= least weight capacity <= sum(weights)
        Do BS until we can do it in days = days
        '''
        l, r = max(weights), sum(weights)
        res = r
        def can_ship(cap):
            ships, cur_cap = 1, cap
            for w in weights:
                if cur_cap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    cur_cap = cap
                cur_cap -= w
            return True


        while l <= r:
            cap = (l + r) // 2
            if can_ship(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        
        return res
