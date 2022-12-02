from bisect import bisect_left, bisect_right

class TimeMap:

    def __init__(self):
        from collections import defaultdict
        self._d = defaultdict(lambda: {"vals": [], "times":[]})

    def set(self, key: str, value: str, timestamp: int) -> None:
        entry = self._d[key]
        pos = bisect_right(entry["times"], timestamp)
        entry["times"].insert(pos, timestamp)
        entry["vals"].insert(pos, value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._d: return ""
        entry = self._d[key]
        pos = bisect_right(entry["times"], timestamp) - 1
        if pos < 0: return ""
        return entry["vals"][pos]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)