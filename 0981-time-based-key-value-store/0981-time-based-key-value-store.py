class TimeMap:
    def __init__(self):
        self.values = collections.defaultdict(list)
        self.times = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append(value)
        self.times[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        pos = bisect.bisect(self.times[key], timestamp)-1
        return self.values[key][pos] if pos>=0 else ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)