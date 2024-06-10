# morning algos
# neetcode time based key-value store

class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = [[value, timestamp]]
        else:
            self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map: return ""
        res = ""
        vals = self.map[key]
        l, r = 0, len(vals) - 1
        while l <= r:
            m = (l + r) // 2
            if vals[m][1] < timestamp:
                res = vals[m][0]
                l = m + 1
            elif vals[m][1] > timestamp:
                r = m - 1
            else:
                return vals[m][0]
        return res




# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)