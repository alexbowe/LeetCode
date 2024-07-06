class FreqStack:

    def __init__(self):
        self._freqs = defaultdict(int)
        self._groups = defaultdict(list)
        self._max_freq = 0

    def push(self, val: int) -> None:
        self._freqs[val] += 1
        self._groups[self._freqs[val]].append(val)
        self._max_freq = max(self._freqs[val], self._max_freq)

    def pop(self) -> int:
        x = self._groups[self._max_freq].pop()
        self._max_freq -= not self._groups[self._max_freq]
        self._freqs[x] -= 1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()