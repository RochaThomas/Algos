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
        values = self.map.get(key, [])
        if not values:
            return ""
        
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] < timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)