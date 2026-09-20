class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        l, r = 0, len(values) - 1
        closest_val = ""
        while l <= r:
            mid = (l + r) // 2
            ts, value = values[mid][1], values[mid][0]
            if ts <= timestamp:
                l = mid + 1
                closest_val = value
            else:
                r = mid - 1
                
        return closest_val
        





