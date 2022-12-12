class TimeMap:

    def __init__(self):
        self._times = collections.defaultdict(list)
        self._values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._times[key].append(timestamp)
        self._values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        pos = bisect.bisect_right(self._times[key], timestamp) - 1
        return self._values[key][pos] if pos >= 0 else ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)