# morning algos
# neetcode time based key-value store

class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key, value, timestamp):
        if key in self.map:
            self.map[key].append([value, timestamp])
        else:
            self.map[key] = [[value, timestamp]]

    def get(self, key, timestamp):
        res = ""
        if key in self.map:
            l, r = 0, len(self.map[key]) - 1
            while l <= r:
                m = (l + r) // 2
                if self.map[key][m][1] <= timestamp:
                    res = self.map[key][m][0]
                    l = m + 1
                else:
                    r = m - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)